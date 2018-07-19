# The points:
points = np.array([[3, -3, 0], [15, 7, 17]]) # Answers: class 0, then class 1
    
def try_our_own_point():
    "Try to predict the class of the point for our own point"
    our_point_fn = tf.estimator.inputs.numpy_input_fn(x={'x':points}, shuffle=False)

    # Make a prediction:
    prediction = classifier.predict(input_fn=our_point_fn)
    return prediction

for index, pred in enumerate(list(try_our_own_point())):
    print(points[index], '→' , pred['class_ids'])