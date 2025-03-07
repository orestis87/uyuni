/**
 * Copyright (c) 2009--2013 Red Hat, Inc.
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

import com.redhat.rhn.common.localization.LocalizationService;
import com.redhat.rhn.domain.rhnpackage.Package;
import com.redhat.rhn.domain.rhnpackage.PackageFactory;
import com.redhat.rhn.domain.rhnpackage.PackageKey;
import com.redhat.rhn.frontend.xmlrpc.serializer.util.SerializerHelper;

import java.io.IOException;
import java.io.Writer;

import redstone.xmlrpc.XmlRpcException;
import redstone.xmlrpc.XmlRpcSerializer;

/**
 *
 * PackageSerializer
 * @xmlrpc.doc
 * #struct_begin("package")
 *      #prop("string", "name")
 *      #prop("string", "version")
 *      #prop("string", "release")
 *      #prop("string", "epoch")
 *      #prop("int", "id")
 *      #prop("string", "arch_label")
 *      #prop("dateTime.iso8601", "last_modified")
 *      #prop_desc("string", "path", "The path on that file system that the package
 *             resides")
 *      #prop_desc("boolean", "part_of_retracted_patch", "True if the package is a part of a retracted patch")
 *      #prop_desc("string", "provider", "The provider of the package, determined by
 *              the gpg key it was signed with.")
 *  #struct_end()
 *
 */
public class PackageSerializer extends RhnXmlRpcCustomSerializer {

    /**
     * {@inheritDoc}
     */
    public Class getSupportedClass() {
        return Package.class;
    }

    /**
     * {@inheritDoc}
     */
    protected void doSerialize(Object value, Writer output, XmlRpcSerializer serializer)
        throws XmlRpcException, IOException {
        Package pack = (Package) value;

        SerializerHelper helper = new SerializerHelper(serializer);
        helper.add("name", pack.getPackageName().getName());
        helper.add("version", pack.getPackageEvr().getVersion());
        helper.add("release", pack.getPackageEvr().getRelease());
        String epoch = pack.getPackageEvr().getEpoch();
        helper.add("epoch", epoch == null ? "" : epoch);
        helper.add("id", pack.getId());
        helper.add("arch_label", pack.getPackageArch().getLabel());
        helper.add("last_modified", pack.getLastModified());
        helper.add("path", pack.getPath());
        helper.add("part_of_retracted_patch", pack.isPartOfRetractedPatch());

        String provider = LocalizationService.getInstance().getMessage(
                "channel.jsp.gpgunknown");
        if (pack.getPackageKeys() != null) {
            for (PackageKey key : pack.getPackageKeys()) {
                if (key.getType().equals(PackageFactory.PACKAGE_KEY_TYPE_GPG) &&
                    key.getProvider() != null) {
                    provider = key.getProvider().getName();
                }
            }
        }
        helper.add("provider", provider);
        helper.writeTo(output);
    }
}
