/**
 * Copyright (c) 2009--2015 Red Hat, Inc.
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
package com.redhat.rhn.frontend.xmlrpc.serializer;


import com.redhat.rhn.frontend.dto.ShortSystemInfo;
import com.redhat.rhn.frontend.xmlrpc.serializer.util.SerializerHelper;

import java.io.IOException;
import java.io.Writer;
import java.util.Date;

import redstone.xmlrpc.XmlRpcException;
import redstone.xmlrpc.XmlRpcSerializer;

/**
 *
 * ShortSystemInfoSerializer
 *
 * @xmlrpc.doc
 *
 * #struct_begin("system")
 *     #prop("int", "id")
 *     #prop("string", "name")
 *     #prop_desc("dateTime.iso8601",  "last_checkin", "Last time server
 *             successfully checked in")
 *     #prop_desc("dateTime.iso8601",  "created", "Server registration time")
 *     #prop_desc("dateTime.iso8601",  "last_boot", "Last server boot time")
 * #struct_end()
 */
public class ShortSystemInfoSerializer extends RhnXmlRpcCustomSerializer {

    /**
     * {@inheritDoc}
     */
    public Class getSupportedClass() {
        return ShortSystemInfo.class;
    }

    /**
     * {@inheritDoc}
     */
    protected void doSerialize(Object value, Writer output, XmlRpcSerializer serializer)
            throws XmlRpcException, IOException {
        ShortSystemInfo system = (ShortSystemInfo) value;
        SerializerHelper helper = new SerializerHelper(serializer);
        helper.add("id", system.getId());
        helper.add("name", system.getName());
        helper.add("last_checkin", system.getLastCheckinDate());

        Date regDate = system.getCreated();
        if (regDate != null) {
            helper.add("created", regDate);
        }

        Date lastBoot = system.getLastBootAsDate();
        if (lastBoot != null) {
            helper.add("last_boot", lastBoot);
        }
        helper.writeTo(output);
    }
}
