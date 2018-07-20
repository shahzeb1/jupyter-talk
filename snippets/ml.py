def deep_classifier():
    '''
    Make a basic tensorflow DNN
    '''
    # Get the data into an np array which makes things easy
    data = np.concatenate((data_points[0], data_points[1]), axis=0)
    labels = np.repeat([0, 1], 200)
    
    # Split into training and testing data:
    x_train, x_test, y_train, y_test = model_selection.train_test_split(
        data, labels, test_size=0.2, random_state=100)
    
    feature_columns = [tf.feature_column.numeric_column('x', shape=np.array(x_train).shape[1:])] 
    
    get_train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={'x':x_train}, y=y_train, num_epochs=5, shuffle=True)
    
    get_test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={'x':x_test}, y=y_test, num_epochs=1, shuffle=True)
    
    # Create a DNN classifier:
    classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns, 
            hidden_units=[1000, 100, 10], n_classes=2, model_dir="model",
            optimizer=tf.train.ProximalAdagradOptimizer(
                learning_rate=0.01,
                l1_regularization_strength=0.01),
                config=tf.estimator.RunConfig().replace(save_summary_steps=10))
    
    # Train the classifier:
    classifier.train(input_fn=get_train_input_fn, steps=1000)

    scores = classifier.evaluate(input_fn=get_test_input_fn)
    
    print('Accuracy (tf.estimator): {0:f}'.format(scores['accuracy']))
    
    return classifier