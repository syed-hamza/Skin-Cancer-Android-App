filepath = "../outputN/weights_part2.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, 
                             save_best_only=True, mode='max',save_weights_only=True)

reduce_lr = ReduceLROnPlateau(monitor='val_accuracy', factor=0.1, patience=3, 
                                   verbose=1, mode='max', min_lr=0.0001)
                              
callbacks_list = [checkpoint, reduce_lr]

history = model.fit_generator(train_generator, steps_per_epoch=train_steps, 
                            validation_data=validation_generator,
                            validation_steps=val_steps,
                            epochs=50, verbose=1,
                            class_weight = class_weights,
                            shuffle=True,  
                            callbacks=callbacks_list)
