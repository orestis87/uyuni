/**
 * Copyright (c) 2009--2012 Red Hat, Inc.
 *
 * This software is licensed to you under the GNU General Public License,
 * version 2 (GPLv2). There is NO WARRANTY for this software, express or
 * implied, including the implied warranties of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
 * along with this software; if not, see
 * http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
 *
 * Red Hat trademarks are not licensed under GPLv2. No permission is
 * granted to use or replicate Red Hat trademarks that are incorporated
 * in this software or its documentation.
 */
package com.redhat.rhn.manager.kickstart.cobbler;

import com.redhat.rhn.common.validator.ValidatorError;
import com.redhat.rhn.domain.kickstart.KickstartData;
import com.redhat.rhn.domain.kickstart.KickstartFactory;
import com.redhat.rhn.domain.user.User;
import com.redhat.rhn.manager.satellite.CobblerSyncCommand;

import org.apache.commons.lang3.StringUtils;
import org.cobbler.Profile;

import java.io.File;

/**
 * KickstartCobblerCommand - class to contain logic to communicate with cobbler
 */
public class CobblerProfileEditCommand extends CobblerProfileCommand {

    private boolean callCobblerSync;

    /**
     * Constructor
     * @param ksDataIn to sync
     * @param userIn - user wanting to sync with cobbler
     */
    public CobblerProfileEditCommand(KickstartData ksDataIn,
            User userIn) {
        this(ksDataIn, userIn, true);
    }

    /**
     * Constructor
     * @param ksDataIn to sync
     * @param userIn - user wanting to sync with cobbler
     * @param cobblerSync - should store() execute a cobbler sync
     */
    public CobblerProfileEditCommand(KickstartData ksDataIn,
            User userIn, boolean cobblerSync) {
        super(ksDataIn, userIn);
        callCobblerSync = cobblerSync;
    }

    /**
     * Call this if you want to use the taskomatic_user.
     *
     * Useful for automated non-user initiated syncs
     * @param ksDataIn to sync
     */
    public CobblerProfileEditCommand(KickstartData ksDataIn) {
        this(ksDataIn, true);
    }

    /**
     * Call this if you want to use the taskomatic_user.
     *
     * Useful for automated non-user initiated syncs
     * @param ksDataIn to sync
     * @param cobblerSync - should store() execute a cobbler sync
     */
    public CobblerProfileEditCommand(KickstartData ksDataIn, boolean cobblerSync) {
        super(ksDataIn);
        callCobblerSync = cobblerSync;
    }

    /**
     * {@inheritDoc}
     */
    public ValidatorError store() {
        if (StringUtils.isBlank(ksData.getCobblerId())) {
            return new CobblerProfileCreateCommand(ksData, user).store();
        }

        Profile prof = Profile.lookupById(getCobblerConnection(), ksData.getCobblerId());
        validateUrl(prof);
        if (prof != null) {
            String cobName = makeCobblerName(ksData);
            String cobFileName = ksData.buildCobblerFileName();
            if (!cobName.equals(prof.getName()) ||
                    !cobFileName.equals(ksData.getCobblerFileName()) ||
                    !(new File(cobFileName)).exists()) {
                // delete current cfg file
                KickstartFactory.removeKickstartTemplatePath(ksData);
                // create new cfg file
                KickstartFactory.saveKickstartData(ksData);
                // change ks profile name
                prof.setName(cobName);
                // change ks profile cfg path
                prof.setKickstart(cobFileName);
            }
            updateCobblerFields(prof);
            if (callCobblerSync) {
                return new CobblerSyncCommand(user).store();
            }
        }
        return null;
    }
}
