'''Randomized quiz competition for 35 students'''

#we need this module for randomly arrangement of the questions
import random

#capitals are dictonary where US states as keys and their capitals as values
def main():
	capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
        	    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
	            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
        	    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
        	    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
        	    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    	            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
        	    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            	    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            	    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
                    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#step 2 - create the quiz file and shuffle the question order

#generate the actual quiz file

	for quizNum in range(3):
    		#create quizz and answer key files
    		quizfile = open("quizzes/capitalquiz%s.txt" % (quizNum + 1),'w')
    		anskeyfile = open("answer_keys/capitalquizzans%s.txt" % (quizNum + 1),'w')

    		#write the header for quizz file
    		quizfile.write('Name :\n\nTime :\n\n')
    		quizfile.write((' ' * 20) + 'State capital quizz (form %s)' % (quizNum + 1))
    		quizfile.write("\n\n")

    		#shuffle the order of the quizz test
    		states = list(capitals.keys())
    		random.shuffle(states)


	#step = 3 create an answer option

	#loop through all the 50 states making a question for each
	for questionNum in range(50):
    		#getting a write or wrong answer
    		correctAnswer = capitals[states[questionNum]]
    		wrongAnswer   = list(capitals.values())
    		del wrongAnswer[wrongAnswer.index(correctAnswer)]
    		wrongAnswer = random.sample(wrongAnswer,3)
    		answerOption = wrongAnswer + [correctAnswer]
    		random.shuffle(answerOption)


	#step = 4 Write Content to the quizz and answer key files
	#Now you have to write the quizz to the quizz files and
	#answer to the answer_key files

	#loop through the 50 states for making a question for each quizz
	for questionNum in range(50):
    	#write the quizz and the answer option to the quizzfile
    	quizfile.write("%s. What is the capital of %s?\n" % (questionNum + 1, states[questionNum]))

    	for i in range(4):
        	quizfile.write("   %s.%s\n" %('ABCD'[i], answerOption[i]))
        	quizfile.write("\n")

    		#write the answer key to the file
    		anskeyfile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOption.index(correctAnswer)]))


	quizfile.close()
	anskeyfile.close()

if __name__ == "__main__":
	main()