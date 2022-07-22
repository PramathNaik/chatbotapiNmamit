function getCurrentTimestamp() {
	return new Date();
}
var msg = document.getElementById('myDIV');
var listen = document.getElementById('listen');

msg.style.display = "block"
function renderMessageToScreen(args) {
	let displayDate = (args.time || getCurrentTimestamp()).toLocaleString('en-IN', {
		month: 'short',
		day: 'numeric',
		hour: 'numeric',
		minute: 'numeric',
	});
	let messagesContainer = $('.messages');

	let message = $(`
	<li class="message ${args.message_side}">
		<div class="avatar"></div>
		<div class="text_wrapper">
			<div class="text">${args.text}</div>
			<div class="timestamp">${displayDate}</div>
		</div>
	</li>
	`);

	messagesContainer.append(message);

	setTimeout(function () {
		message.addClass('appeared');
	}, 0);
	messagesContainer.animate({ scrollTop: messagesContainer.prop('scrollHeight') }, 300);
}

function showUserMessage(message, datetime) {
	renderMessageToScreen({
		text: message,
		time: datetime,
		message_side: 'right',
	});
}

function showBotMessage(message, datetime) {
	renderMessageToScreen({
		text: message,
		time: datetime,
		message_side: 'left',
	});
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$('#send_button').on('click', function (e) {
	showUserMessage($('#msg_input').val());
	msg.style.display = "block"
	$.ajax({
		type: "POST",
		headers: {'X-CSRFToken': csrftoken},
		url: "/bot",
		data: {
			"message": $("#msg_input").val(),
		},
		success: function (data) {
			msg.style.display = "none"
			showBotMessage(data.message);
			
			speakthis(data.message);
		},
	});
	$('#msg_input').val('');
});

$(window).on('load', function () {
	showBotMessage('Namaste! How Can I Help You');
	msg.style.display = "none"
});

var input = document.getElementById("msg_input");

input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("send_button").click();
  }
});
function speakthis(data) {
		var msg = new SpeechSynthesisUtterance(data);
		window.speechSynthesis.speak(msg);
}

	let speechRecognition = new webkitSpeechRecognition();
	let final_transcript = "";
  
	speechRecognition.continuous = true;
	speechRecognition.interimResults = true;
	speechRecognition.lang = 'en-IN';
  
	speechRecognition.onstart = () => {
		listen.style.display = "block"
	};
	speechRecognition.onerror = () => {
	  console.log("Speech Recognition Error");
	};
	speechRecognition.onend = () => {
	  final_transcript = "";
	  listen.style.display = "none"
	  document.querySelector("#msg_input").placeholder = "Say Hi to begin or Tap on microphone to start conversation...";

	};
  
	speechRecognition.onresult = (event) => {
	  let interim_transcript = "";
	    
	  for (let i = event.resultIndex; i < event.results.length; ++i) {
		if (event.results[i].isFinal) {
		  final_transcript += event.results[i][0].transcript;
		  document.querySelector("#msg_input").value = final_transcript;
		  speechRecognition.stop();
		} else {
		  interim_transcript += event.results[i][0].transcript;
		}
	  }
	  document.querySelector("#msg_input").placeholder = interim_transcript;
	  final_transcript = ""
	  interim_transcript = ""
	};


