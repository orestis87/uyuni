/**
 * Copyright (c) 2021 SUSE LLC
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

package com.redhat.rhn.domain.contentmgmt.modulemd;

/**
 * General exception class thrown when an unknown error occurs on a Modulemd API call
 */
public class ModulemdApiException extends Exception {

    /**
     * Initialize a new exception
     */
    public ModulemdApiException() {
        super();
    }

    /**
     * Initialize a new exception
     * @param message the exception message
     */
    public ModulemdApiException(String message) {
        super(message);
    }

    /**
     * Initialize a new exception
     * @param cause the causing throwable
     */
    public ModulemdApiException(Throwable cause) {
        super(cause);
    }
}
