# Copyright (c) 2019-2021 SUSE LLC
# Licensed under the terms of the MIT license.
# This feature is a dependency for:
# - features/secondary/min_monitoring.feature : If this feature fails could let monitoring feature disabled for SLE minion
# - features/secondary/min_centos_monitoring.feature : If this feature fails could let monitoring feature disabled for CentOS minion
# This feature depends on:
# - sumaform : As it is configuring monitoring to be enabled after deployment

@scope_monitoring
Feature: Disable and re-enable monitoring of the server

  Scenario: Log in as admin user
    Given I am authorized for the "Admin" section

  # This assumes that monitoring is enabled via sumaform
  Scenario: Disable monitoring from the UI
    When I follow the left menu "Admin > Manager Configuration > Monitoring"
    And I wait until I see "Server self monitoring" text
    And I click on "Disable"
    And I wait until button "Disable" becomes enabled
    Then I should see a "Monitoring disabled successfully." text
    And I should see a list item with text "System" and a failing bullet
    And I should see a list item with text "PostgreSQL database" and a failing bullet
    And I should see a list item with text "Server self monitoring" and a warning bullet
    And I should see a list item with text "Taskomatic (Java JMX)" and a failing bullet
    And I should see a list item with text "Tomcat (Java JMX)" and a failing bullet
    And I should see a "Restarting Tomcat and Taskomatic is needed for the configuration changes to take effect." text
    And file "/etc/rhn/rhn.conf" should contain "prometheus_monitoring_enabled = 0" on server
    And file "/etc/sysconfig/tomcat" should not contain "Dcom.sun.management.jmxremote.port=3333 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=" on server
    And file "/etc/rhn/taskomatic.conf" should not contain "Dcom.sun.management.jmxremote.port=3334 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=" on server
    And file "/usr/lib/systemd/system/tomcat.service.d/jmx.conf" should not exist on server
    And file "/usr/lib/systemd/system/taskomatic.service.d/jmx.conf" should not exist on server

  Scenario: Restart spacewalk services to apply config changes after disabling monitoring
    When I restart the spacewalk service

  Scenario: Check that monitoring is disabled using the UI
    Given I am authorized for the "Admin" section
    When I follow the left menu "Admin > Manager Configuration > Monitoring"
    And I wait until I see "Server self monitoring" text
    Then I should see a "Enable" button
    And I should see a "Disable" button
    And I should see a list item with text "System" and a failing bullet
    And I should see a list item with text "PostgreSQL database" and a failing bullet
    And I should see a list item with text "Server self monitoring" and a failing bullet
    And I should see a list item with text "Taskomatic (Java JMX)" and a failing bullet
    And I should see a list item with text "Tomcat (Java JMX)" and a failing bullet
    And I should not see a "Restarting Tomcat and Taskomatic is needed for the configuration changes to take effect." text

  Scenario: Enable monitoring from the UI
    When I follow the left menu "Admin > Manager Configuration > Monitoring"
    And I wait until I see "Server self monitoring" text
    And I click on "Enable"
    And I wait until button "Enable" becomes enabled
    Then I should see a "Monitoring enabled successfully." text
    And I should see a list item with text "System" and a success bullet
    And I should see a list item with text "PostgreSQL database" and a success bullet
    And I should see a list item with text "Server self monitoring" and a pending bullet
    And I should see a list item with text "Taskomatic (Java JMX)" and a pending bullet
    And I should see a list item with text "Tomcat (Java JMX)" and a pending bullet
    And I should see a "Restarting Tomcat and Taskomatic is needed for the configuration changes to take effect." text
    And file "/etc/rhn/rhn.conf" should contain "prometheus_monitoring_enabled = 1" on server
    And file "/etc/sysconfig/tomcat" should not contain "Dcom.sun.management.jmxremote.port=3333 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=" on server
    And file "/etc/rhn/taskomatic.conf" should not contain "Dcom.sun.management.jmxremote.port=3334 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=" on server
    And file "/usr/lib/systemd/system/tomcat.service.d/jmx.conf" should contain "jmx_prometheus_javaagent.jar=5556" on server
    And file "/usr/lib/systemd/system/taskomatic.service.d/jmx.conf" should contain "jmx_prometheus_javaagent.jar=5557" on server

  Scenario: Restart spacewalk services to apply config changes after enabling monitoring
    When I restart the spacewalk service

  Scenario: Check that monitoring is enabled using the UI
    Given I am authorized for the "Admin" section
    When I follow the left menu "Admin > Manager Configuration > Monitoring"
    And I wait until I see "Server self monitoring" text
    Then I should see a "Enable" button
    And I should see a "Disable" button
    And I should see a list item with text "System" and a success bullet
    And I should see a list item with text "PostgreSQL database" and a success bullet
    And I should see a list item with text "Server self monitoring" and a success bullet
    And I should see a list item with text "Taskomatic (Java JMX)" and a success bullet
    And I should see a list item with text "Tomcat (Java JMX)" and a success bullet
    And I should not see a "Restarting Tomcat and Taskomatic is needed for the configuration changes to take effect." text
