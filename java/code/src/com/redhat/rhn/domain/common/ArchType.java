/**
 * Copyright (c) 2009--2010 Red Hat, Inc.
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
package com.redhat.rhn.domain.common;

import com.redhat.rhn.domain.BaseDomainHelper;
import com.redhat.rhn.domain.rhnpackage.PackageType;

import org.apache.commons.lang3.builder.ToStringBuilder;

/**
 * ArchType
 */
public class ArchType extends BaseDomainHelper {

    private Long id;
    private String label;
    private String name;

    /**
     * @return Returns the id.
     */
    public Long getId() {
        return id;
    }

    /**
     * @param i The id to set.
     */
    public void setId(Long i) {
        this.id = i;
    }

    /**
     * @return Returns the label.
     */
    public String getLabel() {
        return label;
    }

    /**
     * @param l The label to set.
     */
    public void setLabel(String l) {
        this.label = l;
    }

    /**
     * @return Returns the name.
     */
    public String getName() {
        return name;
    }

    /**
     * @param n The name to set.
     */
    public void setName(String n) {
        this.name = n;
    }


    /**
     * @return returns the package type based on this architecture.
     */
    public PackageType getPackageType() {
        String archType = getLabel();

        if (archType.equals("deb")) {
            return PackageType.DEB;
        }
        else if (archType.equals("rpm")) {
            return PackageType.RPM;
        }
        else {
            throw new RuntimeException("unsupported package type " + archType);
        }
    }


    /** {@inheritDoc} */
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        ArchType archType = (ArchType) o;

        return id != null ? id.equals(archType.id) : archType.id == null;
    }

    /** {@inheritDoc} */
    public int hashCode() {
        return id != null ? id.hashCode() : 0;
    }

    /** {@inheritDoc} */
    public String toString() {
        ToStringBuilder builder = new ToStringBuilder(this);

        builder.append("id", id);
        builder.append("label", label);

        return builder.toString();
    }
}
