Steps to run the code:

1) Open Finetuning_MLP.ipynb in Google Colab

2)output-from-wmt_14_trained_model folder contains the output embeddings from pretrained LSTM-autoencoder. Upload the seven files from output-from-wmt_14_trained_model folder to the google colab (files needs to uploaded individually and no need to upload the folder itself). Upload these files:
	a1.npy
	a2.npy
	a3.npy
	a4.npy
	para.npy
	q.npy
	labels.txt

3) Set Runtime -> Change runtime type -> GPU ->save

4) Select Runtime -> Run all 


Optional: data preprocessing - 
The trained model is very big to upload it on the github. the trained model can be accessed from
https://studentuml-my.sharepoint.com/:f:/g/personal/namrata_shivagunde_student_uml_edu/En3As10JA9BCs505oc4bKiwBReoIAPnrdFqtAoDfdUxb0Q?e=vFAYSS 

It takes around 1 hour to run all the following commands. For ease, I already preprocessed the data and saved all the files in output-from-wmt_14_trained_model folder
and first part of the code is sufficient in itself but if it is needed the data can be processed using the following commands.

Note: Each file has to be processed individually and as the output is generated in the output-demo folder.

These are the same files which are already saved in folder output-from-wmt_14_trained_model, only addition is output labels.txt.

To run the data pre processing part

1) Create virtual environment and install the requirements:

	virtualenv --python=python36 lstmauto_env

	source lstmauto_env/bin/activate

	pip install -r requirements.txt


2) Run the command to get the embeddings for answer 1

	python codify-sentences.py wmt-14-trained-model/model-wmt14/ input-to-model/a1_sents.txt vocabulary.txt output-demo/a1.npy

3) Run the command to get the embeddings for answer 2
	
	python codify-sentences.py wmt-14-trained-model/model-wmt14/ input-to-model/a2_sents.txt vocabulary.txt output-demo/a2.npy

4) Run the command to get the embeddings for answer 3

	python codify-sentences.py wmt-14-trained-model/model-wmt14/ input-to-model/a3_sents.txt vocabulary.txt output-demo/a3.npy

5) Run the command to get the embeddings for answer 4
	
	python codify-sentences.py wmt-14-trained-model/model-wmt14/ input-to-model/a4_sents.txt vocabulary.txt output-demo/a4.npy

6) Run the command to get the embeddings for question
	
	python codify-sentences.py wmt-14-trained-model/model-wmt14/ input-to-model/q_sents.txt vocabulary.txt output-demo/q.npy

7) Run the command to get the embeddings for paragraph

	python codify-para.py wmt-14-trained-model/model-wmt14/ input-to-model/quail_excel.xlsx vocabulary.txt output-demo/para.npy

8)Upload these generated files from output-demo to the google colab

9)Also upload labels.txt given with the submission.

The code has no bugs.
