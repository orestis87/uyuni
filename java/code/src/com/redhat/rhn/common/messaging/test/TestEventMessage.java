/**
 * Copyright (c) 2009--2014 Red Hat, Inc.
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

package com.redhat.rhn.common.messaging.test;

import com.redhat.rhn.common.messaging.EventMessage;

public class TestEventMessage implements EventMessage {

    private boolean msgReceived = false;

    /**
     * {@inheritDoc}
     */
    @Override
    public String toText() {
        return "This is a test";
    }

    /* Check to see if this message was acted upon by
     * the Action class.
     */
    public boolean getMessageReceived() {
        return msgReceived;
    }

    /* The Action should call this message.
     * This is a BAD BAD BAD design pattern to have
     * the Action modify the event but is good for
     * testing because we can determine if the MessageQueue
     * processed this event.
     */
    public void setMessageReceived(boolean msgIn) {
        msgReceived = msgIn;
    }

    /**
     * {@inheritDoc}
     */
    public Long getUserId() {
        return null;
    }

}


