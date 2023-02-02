
<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]

<h3 align="center">Patient Revisit Predictor</h3>

  <p align="center">
    Deep learning prediction of patients revisiting via electronic health records. 
    <br />

  </p>
</div>



## About The Project

This jupyter notebook uses [VetCompass](https://www.vetcompass.org/) data, and simple machine learning architectures to predict if a patients electronic health record can be used to predict is a patient will return to a veterinary practice within a specified time. 

A CNN, LSTM, Bilateral LSTM and Stacked Bidirectional LSTM are trained within this  notebook.

Glove Embedding is used.  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

There are multiple steps for the project to work. It requires access to VetCompass data, which is not publically available. 

### Explanation of files

#### constants.py

All constants used throughout the project. 

#### data_formatter.ipynb

Formats the data from the source to a pandas dataframe which is useable within the project, produces pickles of a test, training and validation dataset. 



## Built With

[![Python][Python.js]][Python-url]
[![Tensorflow][Tensorflow.js]][tensorflow-url]
[![Jupyter][Jupyter.js]][jupyter-url]
[![Pandas][Pandas.js]][pandas-url]
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Aaron Fletcher - [@aaronhafletcher](https://twitter.com/aaronhafletcher) - afletcher@rvc.ac.uk

Project Link: [https://github.com/afletcher53/VC_Patient_Visit_Classifier](https://github.com/afletcher53/VC_Patient_Visit_Classifier)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## References

Coming Soon


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/aaron-fletcher-bvetmed-mrcvs/
[Python.js]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Tensorflow.js]: https://img.shields.io/badge/tensorflow-000000?style=for-the-badge&logo=tensorflow&logoColor=blue
[Tensorflow-url]: https://www.tensorflow.org/
[Jupyter.js]: https://img.shields.io/badge/jupyter-000000?style=for-the-badge&logo=jupyter&logoColor=blue
[Jupyter-url]: https://www.tensorflow.org/
[Pandas.js]: https://img.shields.io/badge/Pandas-000000?style=for-the-badge&logo=Pandas&logoColor=blue
[Pandas-url]: https://pandas.pydata.org/
[product-screenshot]: ./output.png