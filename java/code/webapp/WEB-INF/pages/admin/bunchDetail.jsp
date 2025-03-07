<%@ taglib uri="http://struts.apache.org/tags-html" prefix="html" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://rhn.redhat.com/rhn" prefix="rhn" %>
<%@ taglib uri="http://struts.apache.org/tags-bean" prefix="bean" %>
<%@ taglib uri="http://rhn.redhat.com/tags/list" prefix="rl" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>

<html>
<body>

<rhn:toolbar base="h1" icon="header-taskomatic">
    <bean:message key="bunch.edit.jsp.toolbar" arg0="${fn:escapeXml(label)}"/>
</rhn:toolbar>

<rl:listset name="runList">

       <h2><bean:message key="bunch.edit.jsp.bunchdescription"/></h2>
       <div class="page-summary">
          <c:out value="${bunchdescription}"/>
       </div>
       <div class="text-right">
          <input class="btn btn-default" type="submit" name="dispatch"
            value="<bean:message key='bunch.edit.jsp.button-schedule'/>" />
            <rhn:csrf/>
          <rhn:submitted/>
       </div>
       <hr />
       <br/>
       <div class="page-summary">
          <bean:message key="bunch.jsp.generaldescription"/>
       </div>
    <br/>
    <rl:list
        emptykey="schedule.jsp.noruns"
        dataset="dataset" >
                <rl:decorator name="PageSizeDecorator"/>

                <rl:column sortable="true"
                           bound="false"
                           headerkey="task.edit.jsp.name"
                           sortattr="task" >
                        <c:out value="${current.task}" />
                </rl:column>

                <rl:column bound="false"
                           headerkey="task.edit.jsp.stattime"
                           sortattr="start_time" >
                    <c:choose>
                        <c:when test="${current.start_time == null && current.status == 'INTERRUPTED'}">
                            <bean:message key="bunch.jsp.nullstarttime"/>
                        </c:when>
                        <c:otherwise>
                            <a href="/rhn/admin/ScheduleDetail.do?schid=${current.schedule_id}">
                              <span class="legacy-date-time"><fmt:formatDate pattern="yyyy-MM-dd'T'HH:mm:ssZ" value="${current.start_time}"/></span>
                            </a>
                        </c:otherwise>
                    </c:choose>
                </rl:column>

                <rl:column bound="false"
                           headerkey="task.edit.jsp.endtime"
                           sortattr="end_time" >
                           <span class="legacy-date-time"><fmt:formatDate pattern="yyyy-MM-dd'T'HH:mm:ssZ" value="${current.end_time}"/></span>
                </rl:column>

                <rl:column bound="false"
                           headerkey="kickstart.jsp.status"
                           sortattr="status">
                        <c:out value="${current.status}" />
                </rl:column>

</rl:list>
</rl:listset>

</body>
</html>
