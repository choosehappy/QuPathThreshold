Code associated with the glob post here: http://www.andrewjanowczyk.com/using-qupath-to-help-identify-an-optimal-threshold-for-a-deep-or-machine-learning-classifier/

Digital pathology projects often require assigning a class to cells/objects. For example, you may have a segmentation
of cells/glomeruli/tubules and want to identify the ones which are lymphocytes/sclerotic/distal. This classification 
process can be done using machine or deep learning classifiers by supplying the object of question and receiving an 
output score which indicates the likelihood that that particular object is of that particular type. 

This blog post will demonstrate an efficient way of using QuPath to help find the ideal likelihood threshold for your classifier.
