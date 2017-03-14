$(main());

function main() {
    prepareListeners();
}

function prepareListeners() {
    var acceptButtons = document.querySelectorAll('.accept-button');
    var declineButtons = document.querySelectorAll('.decline-button');
    addInviteResponseListeners(acceptButtons);
    addInviteResponseListeners(declineButtons);
}

function addInviteResponseListeners(buttons) {
    for (var i = 0, len = buttons.length; i < len; i++) {
        var button = buttons[i];
        // using a closure prevents reassignment,
        // allowing for every button to get a listener.
      (function(button) {
        button.addEventListener('click', function() {
            if (button.name.startsWith("accept")) {
                updateGroups(button);
                }
        var parent = button.parentNode.parentNode;
        parent.parentNode.remove(parent);
        // updateInviteAjaxRequest(button);
        });
      })(button);
    }
}

function updateGroups(button) {
    var inviteParent = button.parentNode.parentNode;
    var groupId = inviteParent.action.split('/')[4];
    var groupName = inviteParent.getElementsByClassName('group-name')[0].innerHTML;
    var groupsList = document.getElementById("groups-list");

    var newGroupForm = document.createElement("form");
    newGroupForm.method = "GET";
    newGroupForm.action = "/groupdetails/" + groupId;
    newGroupForm.className = "list-group text-center";

    var newGroupButton = document.createElement("button");
    newGroupButton.type = "button submit";
    newGroupButton.className = "list-group-item";
    newGroupButton.name = "detail_" + groupId;
    var newGroupButtonText = document.createTextNode(groupName);
    newGroupButton.appendChild(newGroupButtonText);

    newGroupForm.appendChild(newGroupButton);
    groupsList.appendChild(newGroupForm);

}
