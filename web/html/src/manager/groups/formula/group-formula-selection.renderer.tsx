import * as React from "react";
import Network from "utils/network";
import { FormulaSelection } from "components/formula-selection";
import { Utils } from "utils/functions";
import SpaRenderer from "core/spa/spa-renderer";

const capitalize = Utils.capitalize;

export const renderer = (renderId, { groupId, warningMessage }) => {
  const messageTexts = {
    formulas_saved: (
      <p>
        {t("Formula saved. Edit configuration options in the enabled formulas and apply the ")}
        <a href={"/rhn/manager/groups/details/highstate?sgid=" + groupId}>{t("Highstate")}</a>
        {t(" for the changes to take effect.")}
      </p>
    ),
    error_invalid_target: t("Invalid target type."),
  };

  function getMessageText(msg) {
    return messageTexts[msg] ? t(messageTexts[msg]) : msg;
  }

  function saveRequest(component, selectedFormulas) {
    const formData: any = {};
    formData.type = "GROUP";
    formData.id = groupId;
    formData.selected = selectedFormulas;

    return Network.post("/rhn/manager/api/formulas/select", formData).then(
      (data) => {
        component.setState({
          messages: data.map((msg) => getMessageText(msg)),
        });
      },
      (xhr) => {
        try {
          component.setState({
            errors: [JSON.parse(xhr.responseText)],
          });
        } catch (err) {
          component.setState({
            errors: [Network.errorMessageByStatus(xhr.status)],
          });
        }
      }
    );
  }

  function addFormulaNavBar(formulaList) {
    jQuery("#formula-nav-bar").remove();

    var navBar = "<ul class='nav nav-tabs nav-tabs-pf' id='formula-nav-bar'>\n";
    navBar +=
      "<li class='active'><a href='/rhn/manager/groups/details/formulas?sgid=" +
      groupId +
      "'>" +
      t("Formulas") +
      "</a></li>\n";
    for (var i in formulaList)
      navBar +=
        "<li><a href='/rhn/manager/groups/details/formula/" +
        i +
        "?sgid=" +
        groupId +
        "'>" +
        capitalize(formulaList[i]) +
        "</a></li>\n";
    navBar += "</ul>";
    jQuery(".spacewalk-content-nav").append(navBar);
  }

  SpaRenderer.renderNavigationReact(
    <FormulaSelection
      dataUrl={"/rhn/manager/api/formulas/list/GROUP/" + groupId}
      saveRequest={saveRequest}
      addFormulaNavBar={addFormulaNavBar}
      warningMessage={warningMessage}
    />,
    document.getElementById(renderId)
  );
};
