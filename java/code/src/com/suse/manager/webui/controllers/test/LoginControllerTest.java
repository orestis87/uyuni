/**
 * Copyright (c) 2019--2021 SUSE LLC
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
package com.suse.manager.webui.controllers.test;

import com.redhat.rhn.common.conf.Config;
import com.redhat.rhn.common.conf.ConfigDefaults;
import com.redhat.rhn.domain.user.User;
import com.redhat.rhn.manager.user.UserManager;
import com.redhat.rhn.testing.RhnMockHttpServletRequest;
import com.redhat.rhn.testing.RhnMockHttpServletResponse;
import com.redhat.rhn.testing.RhnMockHttpSession;
import com.redhat.rhn.testing.UserTestUtils;

import com.suse.manager.webui.controllers.login.LoginController;
import com.suse.manager.webui.utils.LoginHelper;
import com.suse.manager.webui.utils.SparkTestUtils;
import com.suse.utils.Json;

import java.io.UnsupportedEncodingException;
import java.net.URI;
import java.util.HashMap;
import java.util.Map;

import spark.ModelAndView;
import spark.Request;
import spark.RequestResponseFactory;
import spark.Response;
import spark.routematch.RouteMatch;

public class LoginControllerTest extends BaseControllerTestCase {

    @Override
    public void setUp() throws Exception {
        super.setUp();
    }

    public void testUrlBounce() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");

        final String requestUrl = "http://localhost:8080/rhn/manager/login";
        final RouteMatch match = new RouteMatch(new Object(), requestUrl, requestUrl, "");
        final RhnMockHttpServletRequest mockRequest = new RhnMockHttpServletRequest();
        RhnMockHttpSession session = new RhnMockHttpSession();
        mockRequest.setSession(session);

        mockRequest.setRequestURL(requestUrl);
        mockRequest.setupGetMethod("POST");
        mockRequest.setMethod("POST");
        mockRequest.setupPathInfo(URI.create(requestUrl).getPath());
        mockRequest.setupAddParameter("url_bounce", "/rhn/users/UserDetails.do?uid=1");

        response = RequestResponseFactory.create(new RhnMockHttpServletResponse());
        // logging in
        LoginHelper.successfulLogin(mockRequest, response.raw(), user);
        ModelAndView result = LoginController.loginView(RequestResponseFactory.create(match, mockRequest), response);
        HashMap<String, String> model = (HashMap<String, String>) result.getModel();
        assertNotNull(session.getAttribute("webUserID"));
        assertEquals(model.get("url_bounce"), "/rhn/users/UserDetails.do?uid=1");
    }

    public void testLoginWithSSO() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "true");
        final String requestUrl = "http://localhost:8080/rhn/manager/login";
        final RouteMatch match = new RouteMatch(new Object(), requestUrl, requestUrl, "");
        final RhnMockHttpServletRequest mockRequest = new RhnMockHttpServletRequest();
        RhnMockHttpSession session = new RhnMockHttpSession();
        mockRequest.setSession(session);
        mockRequest.setRequestURL(requestUrl);
        mockRequest.setupGetMethod("POST");
        mockRequest.setMethod("POST");
        mockRequest.setupPathInfo(URI.create(requestUrl).getPath());
        mockRequest.setupAddParameter("url_bounce", "/rhn/users/UserDetails.do?uid=1");

        response = RequestResponseFactory.create(new RhnMockHttpServletResponse());
        ModelAndView result = LoginController.loginView(RequestResponseFactory.create(match, mockRequest), response);
        assertNotNull(result); // redirect to the SSO login page
        // we still need to check that the model has been correctly populated
        assertNotNull(((Map<String, Object>) result.getModel()).get("webTheme"));
    }

    public void testUrlBounceNotAuthenticated() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");

        final String requestUrl = "http://localhost:8080/rhn/manager/login";
        final RouteMatch match = new RouteMatch(new Object(), requestUrl, requestUrl, "");
        final RhnMockHttpServletRequest mockRequest = new RhnMockHttpServletRequest();
        RhnMockHttpSession session = new RhnMockHttpSession();
        mockRequest.setSession(session);

        mockRequest.setRequestURL(requestUrl);
        mockRequest.setupGetMethod("POST");
        mockRequest.setMethod("POST");
        mockRequest.setupPathInfo(URI.create(requestUrl).getPath());
        mockRequest.setupAddParameter("url_bounce", "/rhn/users/UserDetails.do?uid=1");

        response = RequestResponseFactory.create(new RhnMockHttpServletResponse());
        ModelAndView result = LoginController.loginView(RequestResponseFactory.create(match, mockRequest), response);
        HashMap<String, String> model = (HashMap<String, String>) result.getModel();
        assertNull(session.getAttribute("webUserID"));
        assertEquals(model.get("url_bounce"), "/rhn/users/UserDetails.do?uid=1");
    }

    public void testLoginOK() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");
        Map<String, String> params = new HashMap<>();
        Request request = SparkTestUtils.createMockRequestWithBody(
                "http://localhost:8080/rhn/manager/api/login",
                new HashMap<String, String>(),
                Json.GSON.toJson(new LoginController.LoginCredentials(user.getLogin(), "password")),
                params);
        Response response = RequestResponseFactory.create(new RhnMockHttpServletResponse());

        String modelView = LoginController.login(request, response);
        LoginController.LoginResult result = Json.GSON.fromJson(modelView, LoginController.LoginResult.class);
        assertTrue(result.isSuccess());
    }

    public void testLoginKO() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");
        Map<String, String> params = new HashMap<>();
        Request request = SparkTestUtils.createMockRequestWithBody(
                "http://localhost:8080/rhn/manager/api/login",
                new HashMap<String, String>(),
                Json.GSON.toJson(new LoginController.LoginCredentials("admin", "wrong")),
                params);
        Response response = RequestResponseFactory.create(new RhnMockHttpServletResponse());

        String modelView = LoginController.login(request, response);
        LoginController.LoginResult result = Json.GSON.fromJson(modelView, LoginController.LoginResult.class);
        assertFalse(result.isSuccess());
        assertEquals("error.invalid_login", String.join("", result.getMessages()));
    }

    public void testLoginWithEmptyPassword() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");
        Map<String, String> params = new HashMap<>();
        Request request = SparkTestUtils.createMockRequestWithBody(
                "http://localhost:8080/rhn/manager/api/login",
                new HashMap<String, String>(),
                Json.GSON.toJson(new LoginController.LoginCredentials("admin", "")),
                params);
        Response response = RequestResponseFactory.create(new RhnMockHttpServletResponse());

        String modelView = LoginController.login(request, response);
        LoginController.LoginResult result = Json.GSON.fromJson(modelView, LoginController.LoginResult.class);
        assertFalse(result.isSuccess());
        assertEquals("error.invalid_login", String.join("", result.getMessages()));
    }

    public void testLoginWithEmptyUsername() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");
        Map<String, String> params = new HashMap<>();
        Request request = SparkTestUtils.createMockRequestWithBody(
                "http://localhost:8080/rhn/manager/api/login",
                new HashMap<String, String>(),
                Json.GSON.toJson(new LoginController.LoginCredentials("admin", "")),
                params);
        Response response = RequestResponseFactory.create(new RhnMockHttpServletResponse());

        String modelView = LoginController.login(request, response);
        LoginController.LoginResult result = Json.GSON.fromJson(modelView, LoginController.LoginResult.class);
        assertFalse(result.isSuccess());
        assertEquals("error.invalid_login", String.join("", result.getMessages()));
    }

    public void testLoginWithInvalidUsername() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");
        Map<String, String> params = new HashMap<>();
        Request request = SparkTestUtils.createMockRequestWithBody(
                "http://localhost:8080/rhn/manager/api/login",
                new HashMap<String, String>(),
                Json.GSON.toJson(new LoginController.LoginCredentials("017324193274913741974",
                        "017324193274913741974")), params);
        Response response = RequestResponseFactory.create(new RhnMockHttpServletResponse());

        String modelView = LoginController.login(request, response);
        LoginController.LoginResult result = Json.GSON.fromJson(modelView, LoginController.LoginResult.class);
        assertFalse(result.isSuccess());
        assertEquals("error.invalid_login", String.join("", result.getMessages()));
    }

    public void testLoginWithDisabledUsername() throws UnsupportedEncodingException {
        Config.get().setBoolean(ConfigDefaults.SINGLE_SIGN_ON_ENABLED, "false");
        User u = UserTestUtils.findNewUser("testUser",
                "testOrg" + this.getClass().getSimpleName());
        UserManager.disableUser(u, u);
        Map<String, String> params = new HashMap<>();
        Request request = SparkTestUtils.createMockRequestWithBody(
                "http://localhost:8080/rhn/manager/api/login",
                new HashMap<String, String>(),
                Json.GSON.toJson(new LoginController.LoginCredentials(u.getLogin(),
                        "password")), params);
        Response response = RequestResponseFactory.create(new RhnMockHttpServletResponse());

        String modelView = LoginController.login(request, response);
        LoginController.LoginResult result = Json.GSON.fromJson(modelView, LoginController.LoginResult.class);
        assertFalse(result.isSuccess());
        assertEquals("account.disabled", String.join("", result.getMessages()));
    }
}
