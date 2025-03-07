/**
 * Copyright (c) 2009--2017 Red Hat, Inc.
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
package com.redhat.rhn.common.security.acl.test;

import com.redhat.rhn.common.conf.Config;
import com.redhat.rhn.common.security.acl.Access;
import com.redhat.rhn.common.security.acl.Acl;
import com.redhat.rhn.domain.channel.Channel;
import com.redhat.rhn.domain.channel.Modules;
import com.redhat.rhn.domain.channel.test.ChannelFactoryTest;
import com.redhat.rhn.domain.role.Role;
import com.redhat.rhn.domain.role.RoleFactory;
import com.redhat.rhn.domain.server.Server;
import com.redhat.rhn.domain.server.ServerConstants;
import com.redhat.rhn.domain.server.test.ServerFactoryTest;
import com.redhat.rhn.domain.user.User;
import com.redhat.rhn.domain.user.legacy.UserImpl;
import com.redhat.rhn.manager.entitlement.EntitlementManager;
import com.redhat.rhn.manager.formula.FormulaManager;
import com.redhat.rhn.manager.formula.FormulaMonitoringManager;
import com.redhat.rhn.manager.system.ServerGroupManager;
import com.redhat.rhn.manager.system.SystemManager;
import com.redhat.rhn.manager.system.entitling.SystemEntitlementManager;
import com.redhat.rhn.manager.system.entitling.SystemEntitler;
import com.redhat.rhn.manager.system.entitling.SystemUnentitler;
import com.redhat.rhn.testing.BaseTestCaseWithUser;
import com.redhat.rhn.testing.ServerTestUtils;
import com.redhat.rhn.testing.TestUtils;
import com.redhat.rhn.testing.UserTestUtils;

import com.suse.manager.clusters.ClusterManager;
import com.suse.manager.virtualization.VirtManagerSalt;
import com.suse.manager.webui.services.iface.MonitoringManager;
import com.suse.manager.webui.services.iface.SaltApi;
import com.suse.manager.webui.services.iface.SystemQuery;
import com.suse.manager.webui.services.iface.VirtManager;
import com.suse.manager.webui.services.test.TestSaltApi;
import com.suse.manager.webui.services.test.TestSystemQuery;

import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * AccessTest
 */
public class AccessTest extends BaseTestCaseWithUser {

    private Acl acl;
    private final SystemQuery systemQuery = new TestSystemQuery();
    private final SaltApi saltApi = new TestSaltApi();
    private final ServerGroupManager serverGroupManager = new ServerGroupManager();
    private final FormulaManager formulaManager = new FormulaManager(saltApi);
    private final ClusterManager clusterManager = new ClusterManager(
            saltApi, systemQuery, serverGroupManager, formulaManager);
    private final VirtManager virtManager = new VirtManagerSalt(saltApi);
    private final MonitoringManager monitoringManager = new FormulaMonitoringManager();
    private final SystemEntitlementManager systemEntitlementManager = new SystemEntitlementManager(
            new SystemUnentitler(virtManager, monitoringManager, serverGroupManager),
            new SystemEntitler(saltApi, virtManager, monitoringManager, serverGroupManager)
    );

    @Override
    public void setUp() throws Exception {
        super.setUp();
        acl = new Acl();
        acl.registerHandler(new Access(clusterManager));
    }

    public void testAccessNotFoundEntry() {
        Access access = new Access(clusterManager);
        String[] foo = {"FOO"};
        boolean rc = access.aclIs(null, foo);
        assertFalse(rc);
    }

    public void testAccessValidEntry() {
        Config c = Config.get();
        c.setBoolean("test.true", "true");
        c.setBoolean("test.TrUe", "TrUe");
        c.setBoolean("test.one", "1");
        c.setBoolean("test.yes", "y");
        c.setBoolean("test.YES", "Y");
        c.setBoolean("test.on", "on");
        c.setBoolean("test.ON", "ON");

        Access access = new Access(clusterManager);
        String[] foo = new String[1];

        foo[0] = "test.true";
        assertTrue("test.true is false", access.aclIs(null, foo));
        foo[0] = "test.TrUe";
        assertTrue("test.TrUe is false", access.aclIs(null, foo));
        foo[0] = "test.one";
        assertTrue("test.one is false", access.aclIs(null, foo));
        foo[0] = "test.yes";
        assertTrue("test.yes is false", access.aclIs(null, foo));
        foo[0] = "test.YES";
        assertTrue("test.YES is false", access.aclIs(null, foo));
        foo[0] = "test.on";
        assertTrue("test.on is false", access.aclIs(null, foo));
        foo[0] = "test.ON";
        assertTrue("test.ON is false", access.aclIs(null, foo));
    }

    public void testAccessWithInvalidAcl() {
        Map context = new HashMap();
        boolean rc = acl.evalAcl(context, "is(foo)");
        assertFalse(rc);
    }

    public void testAccessWithValidAcl() {
        Config c = Config.get();
        c.setBoolean("test.true", "true");
        c.setBoolean("test.TrUe", "TrUe");
        c.setBoolean("test.one", "1");
        c.setBoolean("test.yes", "y");
        c.setBoolean("test.YES", "Y");
        c.setBoolean("test.on", "on");
        c.setBoolean("test.ON", "ON");

        Map context = new HashMap();

        assertTrue("test.true is false", acl.evalAcl(context, "is(test.true)"));
        assertTrue("test.TrUe is false", acl.evalAcl(context, "is(test.TrUe)"));
        assertTrue("test.one is false", acl.evalAcl(context, "is(test.one)"));
        assertTrue("test.yes is false", acl.evalAcl(context, "is(test.yes)"));
        assertTrue("test.YES is false", acl.evalAcl(context, "is(test.YES)"));
        assertTrue("test.on is false", acl.evalAcl(context, "is(test.on)"));
        assertTrue("test.ON is false", acl.evalAcl(context, "is(test.ON)"));
    }

    public void testForFalse() {
        Config c = Config.get();
        c.setBoolean("test.false", "false");
        c.setBoolean("test.FaLse", "FaLse");
        c.setBoolean("test.zero", "0");
        c.setBoolean("test.no", "n");
        c.setBoolean("test.NO", "N");
        c.setBoolean("test.off", "off");
        c.setBoolean("test.OFF", "OFF");

        Map context = new HashMap();

        assertFalse("test.false is true", acl.evalAcl(context, "is(test.false)"));
        assertFalse("test.FaLse is true", acl.evalAcl(context, "is(test.FaLse)"));
        assertFalse("test.zero is true", acl.evalAcl(context, "is(test.zero)"));
        assertFalse("test.no is true", acl.evalAcl(context, "is(test.no)"));
        assertFalse("test.NO is true", acl.evalAcl(context, "is(test.NO)"));
        assertFalse("test.off is true", acl.evalAcl(context, "is(test.off)"));
        assertFalse("test.OFF is true", acl.evalAcl(context, "is(test.OFF)"));
    }

    public void testUserRoleAcl() {
        Map context = new HashMap();
        User user = new MockUser();
        user.addPermanentRole(RoleFactory.ORG_ADMIN);
        context.put("user", user);
        boolean rc = acl.evalAcl(context, "user_role(org_admin)");
        assertTrue(rc);
    }

    public void testUserCanManageChannelAcl() {
        Map context = new HashMap();
        User user =  UserTestUtils.findNewUser("testUser",
                "testOrg" + this.getClass().getSimpleName());
        user.addPermanentRole(RoleFactory.CHANNEL_ADMIN);
        context.put("user", user);
        boolean rc = acl.evalAcl(context, "user_can_manage_channels()");
        assertTrue(rc);
    }

    public void testUserRoleAclFalse() {
        Map context = new HashMap();
        User user = new MockUser();
        user.addPermanentRole(RoleFactory.ORG_ADMIN);
        context.put("user", user);
        boolean rc = acl.evalAcl(context, "user_role(channel_admin)");
        assertFalse(rc);
    }

    public void testNeedsFirstUser() {
        boolean rc = acl.evalAcl(new HashMap(), "need_first_user()");
        assertFalse(rc);
    }

    public void testSystemFeature() throws Exception {
        Map context = new HashMap();
        User user = UserTestUtils.findNewUser("testUser",
                "testOrg" + this.getClass().getSimpleName());
        context.put("user", user);
        Server s = ServerFactoryTest.createTestServer(user, false);
        context.put("sid", new String[] {s.getId().toString()});
        boolean rc = acl.evalAcl(context, "system_feature(ftr_kickstart)");
        assertTrue(rc);
        rc = acl.evalAcl(context, "not system_feature(ftr_kickstart)");
        assertFalse(rc);
    }

    public void testAclSystemHasManagementEntitlement() throws Exception {
        Map context = new HashMap();

        User user = UserTestUtils.findNewUser("testUser",
                "testOrg" + this.getClass().getSimpleName());

        Server s = ServerFactoryTest.createTestServer(user, true,
                ServerConstants.getServerGroupTypeEnterpriseEntitled());
        context.put("sid", new String[] {s.getId().toString()});
        context.put("user", user);
        assertTrue(acl.evalAcl(context, "system_has_management_entitlement()"));

        s = ServerFactoryTest.createUnentitledTestServer(user, true,
                ServerFactoryTest.TYPE_SERVER_NORMAL, new Date());
        context.put("sid", new String[] {s.getId().toString()});
        assertFalse(acl.evalAcl(context, "system_has_management_entitlement()"));


    }

    /**
     * Test ACL: system_has_salt_entitlement()
     * @throws Exception in case of an error
     */
    public void testAclSystemHasSaltEntitlement() throws Exception {
        Map<String, Object> context = new HashMap<>();
        User user = UserTestUtils.findNewUser("testUser",
                "testOrg" + this.getClass().getSimpleName());

        // Check with a salt entitled system
        Server s = ServerFactoryTest.createTestServer(user, true,
                ServerConstants.getServerGroupTypeSaltEntitled());
        context.put("sid", new String[] {s.getId().toString()});
        context.put("user", user);
        assertTrue(acl.evalAcl(context, "system_has_salt_entitlement()"));

        // Change the base entitlement to MANAGEMENT
        systemEntitlementManager.setBaseEntitlement(s, EntitlementManager.MANAGEMENT);
        context.put("sid", new String[] {s.getId().toString()});
        context.put("user", user);
        assertFalse(acl.evalAcl(context, "system_has_salt_entitlement()"));

        // Check with an unentitled system
        s = ServerFactoryTest.createUnentitledTestServer(user, true,
                ServerFactoryTest.TYPE_SERVER_NORMAL, new Date());
        context.put("sid", new String[] {s.getId().toString()});
        assertFalse(acl.evalAcl(context, "system_has_salt_entitlement()"));
    }

    /**
     * Test ACL: acl_system_is_bootstrap_minion_server()
     * @throws Exception in case of an error
     */
    public void testAclSystemIsBootstrapMinionServer() throws Exception {
        Map<String, Object> context = new HashMap<>();
        User user = UserTestUtils.findNewUser("testUser",
                "testOrg" + this.getClass().getSimpleName());

        // Check with a minion system w/o bootstrap entitlement
        Server s = ServerTestUtils.createTestSystem(user, ServerConstants.getServerGroupTypeBootstrapEntitled());
        s = TestUtils.saveAndReload(s);

        context.put("sid", new String[] {s.getId().toString()});
        context.put("user", user);
        assertFalse(acl.evalAcl(context, "system_is_bootstrap_minion_server()"));

        // Check with a minion system with bootstrap entitlement
        SystemManager.addMinionInfoToServer(s.getId(), "testMid");
        s = TestUtils.saveAndReload(s);

        assertTrue(acl.evalAcl(context, "system_is_bootstrap_minion_server()"));

        // Check with a traditional system system
        s = ServerFactoryTest.createUnentitledTestServer(user, true,
                ServerFactoryTest.TYPE_SERVER_NORMAL, new Date());
        context.put("sid", new String[] {s.getId().toString()});
        assertFalse(acl.evalAcl(context, "system_is_bootstrap_minion_server()"));
    }

    public void testUnimplementedMethods() {

        String[] methods = { "user_authenticated()" };

        for (int i = 0; i < methods.length; i++) {
            evalAclAssertFalse(acl, methods[i]);
        }
    }

    public void testGlobalConfigIsGone() {
        Map context = new HashMap();
        try {
            acl.evalAcl(context, "global_config(foo)");
            fail("global_config is back, what moron undid my change!");
        }
        catch (IllegalArgumentException e) {
            // doo nothing
        }
    }

    public void testCanAccessChannel() {
        try {
            Map context = new HashMap();
            User user =  UserTestUtils.findNewUser("testUser",
                    "testOrg" + this.getClass().getSimpleName());
            context.put("user", user);
            user.addPermanentRole(RoleFactory.CHANNEL_ADMIN);

            Channel chan = ChannelFactoryTest.createBaseChannel(user);
            assertTrue(acl.evalAcl(context, "can_access_channel(" + chan.getId() + ")"));
        }
        catch (Exception e) {
            fail("channel validation failed");
        }
    }

    public void testIsModularChannel() {
        Map context = new HashMap();
        User user = UserTestUtils.findNewUser("testUser", "testOrg" + this.getClass().getSimpleName());
        context.put("user", user);

        user.addPermanentRole(RoleFactory.CHANNEL_ADMIN);
        Channel chan = null;

        try {
            chan = ChannelFactoryTest.createTestChannel(user);
        }
        catch (Exception e) {
            fail("channel validation failed");
        }

        context.put("cid", chan.getId());

        assertFalse(acl.evalAcl(context, "is_modular_channel()"));

        Modules mod = new Modules();
        mod.setRelativeFilename("filename");
        chan.setModules(mod);
        mod.setChannel(chan);

        assertTrue(acl.evalAcl(context, "is_modular_channel()"));

    }

    public void testFormvarExists() {
        Map context = new HashMap();
        assertFalse(acl.evalAcl(context, "formvar_exists(cid)"));
        context.put("cid", "161");
        assertTrue(acl.evalAcl(context, "formvar_exists(cid)"));
        assertFalse(acl.evalAcl(context, "formvar_exists(pid)"));
        assertFalse(acl.evalAcl(context, "formvar_exists()"));
    }

    private void evalAclAssertFalse(Acl aclIn, String aclStr) {
        Map context = new HashMap();
        // acl methods must be in the following form
        // aclXxxYyy(Object context, String[] params) and invoked
        // xxx_yyy(param);
        boolean rc = aclIn.evalAcl(context, aclStr);
        assertFalse(rc);
    }

    public void testIsVirtual() throws Exception {
        Server host = ServerTestUtils.createVirtHostWithGuests(user, 1, systemEntitlementManager);
        Server guest = host.getGuests().iterator().next().getGuestSystem();

        Access a = new Access(clusterManager);
        Map ctx = new HashMap();
        ctx.put("sid", guest.getId());
        ctx.put("user", user);
        assertTrue(a.aclSystemIsVirtual(ctx, null));
    }

    /**
     * Override the methods in User that talk to the database
     */
    class MockUser extends UserImpl {
        private final Set mockRoles;

        MockUser() {
            mockRoles = new HashSet();
        }

        /**
         * This is the key method that needs to be overriden
         * There is a check in User that looks up the Org
         * that isn't necessary for this Unit Test
         */
        @Override
        public void addPermanentRole(Role label) {
            mockRoles.add(label);
        }

        /** @see com.redhat.rhn.domain.user.User#hasRole */
        @Override
        public boolean hasRole(Role label) {
            return mockRoles.contains(label);
        }
    }


}
