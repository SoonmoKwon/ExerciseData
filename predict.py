# -*- coding: utf-8 -*-
import kenlm

def predict(model_path, voc_path):
	# load language model with KenLM
	model = kenlm.Model(model_path)
	print ("Language Model at " + model_path + "loaded.")

	# load vocabulary (or load word list)
	voc = []
	file_reader = open(voc_path, "r", encoding='utf-8')
	for line in file_reader:
		voc.append(line.strip())
	print ("Vocabulary at " + voc_path + "loaded\n")

    sequence = input("Sequence: ")

	print ("Given sequence: " + sequence)

	# prediction loop
	loop_condition = True
	while loop_condition:
		score_current = model.score(sequence, bos=True, eos=False)
		score_end = model.score(sequence, bos=True, eos=True)

		score_next = score_end
		seqeunce_next = sequence

		for word in voc:
			sequence_cand = sequence + " " + word
			score_cand = model.score(sequence_cand, bos=True, eos=False)
			if score_cand > score_next:
				score_next = score_cand
				sequence_next = sequence_cand

		if score_next > score_end:
			sequence = sequence_next
		else:
			loop_condition = False

	print ("Result: " + sequence)

	return

def main():
    modelname = input("Type the model name you would use: ")
	model_path = modelname
	voc_path = 'sonagi.voc'

	predict(model_path, voc_path)

	return

if __name__ == "__main__":
	main()
