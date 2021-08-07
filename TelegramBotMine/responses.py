import re

def process_message(message, response_array, response):
	list_message = re.findall(r"[\w']+|[.,!?]", message.lower())

	score = 0
	for word in list_message:
		if word in response_array:
			score = score + 1

	print(score, response)
	return [score, response]


def get_response(message):
	response_list = [
		process_message(message, ['hello', 'hi', 'hey', 'good day', "what's up", 'up' "what is up", "how's going", 'how is going'], 'Hey there!what can I help you'),
		process_message(message, ['bye', 'good bye', 'see ya!', 'see you later', 'see you soon', 'see you again'], 'Bye see you later'),
		process_message(message, ['ip'], 'IP Server: mohaborey.aternos.me'),
		process_message(message, ['port'], 'Port Server: 19670')
	]


	response_scores = []
	for response in response_list:
		response_scores.append(response[0])


	winning_response = max(response_scores)
	matching_response = response_list[response_scores.index(winning_response)]

	if winning_response == 0:
		bot_response = 'I did\'t understand what you want.'
	else:
		bot_response = matching_response[1]

	print('Bot response:', bot_response)
	return bot_response


#get_respone('Helo')