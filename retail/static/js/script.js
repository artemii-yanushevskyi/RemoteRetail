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
		
		</table>`;
	}
	else {
		html = purchasesTable;
	}
	return html;
}