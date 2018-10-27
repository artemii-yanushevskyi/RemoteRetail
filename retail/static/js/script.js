/*function daytime() {
	var date = new Date();
	var current_hour = date.getHours();
	var result = "evening"
	if (current_hour < 6) {
		result = "night"
	} else if (current_hour < 12) {
		result = "morning"
	} else if (current_hour < 6) {
		result = "afternoon"
	}
	return result
}*/

function WritePurchasesTable(purchasesTable) {
if (typeof purchasesTable === "object") {
	html = `
	<table>
    <tbody>\n`;
    for (var key in purchasesTable) {
      html += "<tr>\n";
      html += "  <td>" + key + "</td>\n";
      html += "  <td " + "</td>\n";
      html += "</tr>\n\n";
    }
    html += `
    </tbody>
	</table>`;
}
else {
	html = purchasesTable;
}
return html;
}