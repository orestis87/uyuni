import * as React from "react";
import { Highlight } from "components/table/Highlight";
import { ChannelAnchorLink } from "components/links";
import { ChannelsTreeType } from "core/channels/api/use-channels-tree-api";
import { ChannelType } from "core/channels/type/channels.type";
import { RequiredChannelsResultType } from "core/channels/api/use-mandatory-channels-api";

type PropsType = {
  base: ChannelType;
  search: string;
  childChannelsId: Array<number>;
  selectedChannelsIdsInGroup: Array<number>;
  onChannelToggle: Function;
  channelsTree: ChannelsTreeType;
  requiredChannelsResult: RequiredChannelsResultType;
};

const ChildChannels = (props: PropsType) => {
  if (props.childChannelsId.length === 0) {
    return <span>&nbsp;{t("no child channels")}</span>;
  }

  const { requiredChannels, dependenciesTooltip } = props.requiredChannelsResult;

  return (
    <>
      {props.childChannelsId
        .map((cId: number): ChannelType => props.channelsTree.channelsById[cId])
        .map((c) => {
          const toolTip = dependenciesTooltip(c.id, Object.values(props.channelsTree.channelsById));
          const mandatoryChannelsForBaseId: Set<number> | null | undefined =
            props.base && requiredChannels.get(props.base.id);
          const isMandatory = mandatoryChannelsForBaseId && mandatoryChannelsForBaseId.has(c.id);
          return (
            <div key={c.id} className="checkbox">
              <input
                type="checkbox"
                value={c.id}
                id={"child_" + c.id}
                name="childChannels"
                checked={props.selectedChannelsIdsInGroup.includes(c.id)}
                onChange={(event) => props.onChannelToggle(parseInt(event.target.value, 10))}
              />
              <label title={toolTip} htmlFor={"child_" + c.id}>
                <Highlight enabled={(props.search || "").length > 0} text={c.name} highlight={props.search}></Highlight>
              </label>
              &nbsp;
              {toolTip ? ( // eslint-disable-next-line jsx-a11y/anchor-is-valid
                <a href="#">
                  <i className="fa fa-info-circle spacewalk-help-link" title={toolTip}></i>
                </a>
              ) : null}
              &nbsp;
              {c.recommended ? (
                <span className="recommended-tag-base" title={t("This channel is recommended")}>
                  {t("recommended")}
                </span>
              ) : null}
              {isMandatory ? (
                <span className="mandatory-tag-base" title={t("This channel is mandatory")}>
                  {t("mandatory")}
                </span>
              ) : null}
              <ChannelAnchorLink id={c.id} newWindow={true} />
            </div>
          );
        })}
    </>
  );
};

export default ChildChannels;
