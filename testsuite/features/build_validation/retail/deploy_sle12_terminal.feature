# Copyright (c) 2021 SUSE LLC
# Licensed under the terms of the MIT license.

@proxy
@private_net
@sle12sp5_terminal
Feature: PXE boot a SLES 12 SP5 retail terminal
  In order to use SUSE Manager for Retail solution
  As the system administrator
  I PXE boot one of the terminals
  I perform a mass import of several virtual terminals and one real minion

  Scenario: Configure image-synchronization formula at branch server for SLE12 SP5 terminal deplyoment
    When I execute "image_sync" for "SLE12 SP5" via semi-xmlrpc-tester

  Scenario: Prepare branch server for SLE12 SP5 terminal deployment
    When I execute "prepare" for "SLE12 SP5" via semi-xmlrpc-tester

  Scenario: Log in as admin user
    Given I am authorized for the "Admin" section

  Scenario: PXE boot the SLES 12 SP5 retail terminal
    When I run "reboot" on "sle12sp5_terminal"
    And I wait at most 180 seconds until Salt master sees "sle12sp5_terminal" as "unaccepted"
    And I accept "sle12sp5_terminal" key in the Salt master
    And I follow the left menu "Systems > Overview"
    And I wait until I see the name of "sle12sp5_terminal", refreshing the page
    And I follow this "sle12sp5_terminal" link
    And I wait until event "Apply states [util.syncstates, saltboot] scheduled" is completed
    And I follow "Software" in the content area
    And I follow "Software Channels" in the content area
    And I wait until radio button "SLES12-SP5-Pool" is checked, refreshing the page
    And I wait until event "Package List Refresh scheduled" is completed
    Then the PXE boot minion should have been reformatted

  Scenario: Check connection from SLES 12 SP5 retail terminal to branch server
    Given I am on the Systems overview page of this "sle12sp5_terminal"
    When I follow "Details" in the content area
    And I follow "Connection" in the content area
    Then I should see "proxy" short hostname

  Scenario: Install a package on the SLES 12 SP5 retail terminal
    When I follow "Software" in the content area
    And I follow "Install"
    And I enter "gcc" as the filtered package name
    And I check "gcc-4.8" in the list
    And I click on "Install Selected Packages"
    And I click on "Confirm"
    Then I should see a "1 package install has been scheduled" text
    When I wait until event "Package Install/Upgrade scheduled" is completed

  Scenario: Remove a package on the SLES 12 SP5 retail terminal
    When I follow "Software" in the content area
    And I follow "List / Remove"
    And I enter "gcc" as the filtered package name
    And I click on the filter button
    And I check "gcc-4.8" in the list
    And I click on "Remove Packages"
    And I click on "Confirm"
    Then I should see a "1 package removal has been scheduled" text
    When I wait until event "Package Removal scheduled" is completed
