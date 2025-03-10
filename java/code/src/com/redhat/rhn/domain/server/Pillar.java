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
package com.redhat.rhn.domain.server;

import com.redhat.rhn.domain.Identifiable;
import com.redhat.rhn.domain.org.Org;

import com.vladmihalcea.hibernate.type.json.JsonType;

import org.hibernate.annotations.Type;
import org.hibernate.annotations.TypeDef;
import org.hibernate.annotations.TypeDefs;

import java.util.Map;
import java.util.TreeMap;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.SequenceGenerator;
import javax.persistence.Table;


/**
 * Pillar - Class representation of the table suseSaltPillars entries
 *
 * https://github.com/uyuni-project/uyuni-rfc/pull/51
 */

@TypeDefs({
        @TypeDef(name = "json", typeClass = JsonType.class)
})
@Entity
@Table(name = "suseSaltPillar")
public class Pillar implements Identifiable {

    @Id
    @GeneratedValue(generator = "pillar_seq")
    @SequenceGenerator(name = "pillar_seq", sequenceName = "suse_salt_pillar_id_seq", allocationSize = 1)
    @Column(name = "id")
    private Long id;

    @ManyToOne
    @JoinColumn(name = "server_id")
    private MinionServer minion;

    @ManyToOne
    @JoinColumn(name = "org_id")
    private Org org;

    @ManyToOne
    @JoinColumn(name = "group_id")
    private ServerGroup group;

    @Column(name = "category")
    private String category;

    @Type(type = "json")
    @Column(columnDefinition = "jsonb")
    private Map<String, Object> pillar = new TreeMap<>();

    /**
     * Default constructor. Mostly for hibernate use.
     */
    public Pillar() {
        initPillar(null, null, null, null, null);
    }

    /**
     * Constructor for global pillar
     *
     * @param categoryIn category of the pillar
     * @param pillarIn data in JSON format
     */
    public Pillar(String categoryIn, Map<String, Object> pillarIn) {
        initPillar(categoryIn, pillarIn, null, null, null);
    }

    /**
     * Constructor for minion pillar
     *
     * @param categoryIn category of the pillar
     * @param pillarIn pillar data in JSON format
     * @param minionIn MinionServer owner of the pillar
     */
    public Pillar(String categoryIn, Map<String, Object> pillarIn, MinionServer minionIn) {
        initPillar(categoryIn, pillarIn, minionIn, null, null);
    }

    /**
     * Constructor for system group pillar
     *
     * @param categoryIn category of the pillar
     * @param pillarIn pillar data in JSON format
     * @param groupIn ServerGroup owning the pillar
     */
    public Pillar(String categoryIn, Map<String, Object> pillarIn, ServerGroup groupIn) {
        initPillar(categoryIn, pillarIn, null, groupIn, null);
    }

    /**
     * Constructor for organization pillar
     *
     * @param categoryIn category of the pillar
     * @param pillarIn pillar data in JSON format
     * @param orgIn organization owning the pillar
     */
    public Pillar(String categoryIn, Map<String, Object> pillarIn, Org orgIn) {
        initPillar(categoryIn, pillarIn, null, null, orgIn);
    }

    private void initPillar(String categoryIn, Map<String, Object> pillarIn,
                            MinionServer serverIn,
                            ServerGroup groupIn, Org orgIn) {
        this.category = categoryIn;
        this.pillar = pillarIn;
        this.minion = serverIn;
        this.org = orgIn;
        this.group = groupIn;
    }

    public Long getId() {
        return id;
    }
    public void setId(Long idIn) {
        this.id = idIn;
    }

    public boolean isMinionPillar() {
        return minion != null;
    }

    public boolean isGroupPillar() {
        return group != null;
    }

    public boolean isOrgPillar() {
        return org != null;
    }

    public boolean isGlobalPillar() {
        return minion == null && group == null && org == null;
    }

    /**
     * Set pillar as group pillar and its owning group
     *
     * This removes any other owners and changes pillar to group pillar
     * @param groupIn SystemGroup owner of the pillar
     * @return itself
     */
    public Pillar setGroup(ServerGroup groupIn) {
        this.group = groupIn;
        this.org = null;
        this.minion = null;
        return this;
    }

    /**
     * Set pillar as organization pillar and its owning organization
     *
     * This removes any other owners and changes pillar to organization pillar
     * @param orgIn Org owner of the pillar
     * @return itself
     */
    public Pillar setOrg(Org orgIn) {
        this.org = orgIn;
        this.group = null;
        this.minion = null;
        return this;
    }

    /**
     * Set pillar as minion pillar and its owning minion
     *
     * This removes any other owners and changes pillar to minion pillar
     * @param minionIn MinionServer owner of the pillar
     * @return itself
     */
    public Pillar setMinion(MinionServer minionIn) {
        this.minion = minionIn;
        this.group = null;
        this.org = null;
        return this;
    }

    /**
     * Set pillar as global pillar and remove any owner
     *
     * This removes previous owner and changes pillar to global pillar
     * @return itself
     */
    public Pillar setGlobal() {
        this.minion = null;
        this.group = null;
        this.org = null;
        return this;
    }

    /**
     * Get pillar value in JSON format
     *
     * @return pillar value
     */
    public Map<String, Object> getPillar() {
        return pillar;
    }

    /**
     * Set pillar value
     *
     * @param pillarIn pillar value in JSON format
     * @return itself
     */
    public Pillar setPillar(Map<String, Object> pillarIn) {
        this.pillar = pillarIn;
        return this;
    }

    /**
     * Get pillar category
     *
     * @see #setCategory
     * @return pillar category name
     */
    public String getCategory() {
        return category;
    }

    /**
     * Set pillar category
     *
     * Category is helper construct that each generator class can maintain their own pillar under its own category
     * and does not need to concert itself with merging pillar data into one pillar.
     *
     * @param categoryIn category name
     * @return itself
     */
    public Pillar setCategory(String categoryIn) {
        this.category = categoryIn;
        return this;
    }

    /**
     * Add an entry at the pillar root level.
     *
     * @param key the pillar name
     * @param value the pillar value
     */
    public void add(String key, Object value) {
        getPillar().put(key, value);
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public String toString() {
        return pillar.toString();
    }
}

