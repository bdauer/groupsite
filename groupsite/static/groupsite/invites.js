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
            updateInviteAjaxRequest(button);
            if (button.name.startsWith("accept")) {
                updateGroups(button);
                }
        var parent = button.parentNode.parentNode;
        parent.parentNode.remove(parent);


        });
      })(button);
    }
}
/**
Update groups after an invite is accepted.
*/
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

function updateInviteAjaxRequest(button) {
    var vals = button.name.split('_')
    var newStatus = vals[0];
    var inviteId = vals[1];

    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });
    var csrftoken = getCookieValue('csrftoken');
    $.ajax({
        url: 'updateinvite/',
        type: 'POST',
        data: {
            'invite_id': inviteId,
            'new_status': newStatus
        }
    })
};

function getCookieValue(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      console.log(cookies)
      for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}



function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
