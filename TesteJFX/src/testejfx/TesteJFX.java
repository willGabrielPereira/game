/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testejfx;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.Background;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

/**
 *
 * @author User
 */
public class TesteJFX extends Application{
    
    private Scene scene;
    
    @Override
    public void start(Stage primaryStage) {
        
        
        primaryStage.setTitle("Title");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    
    public void initComponents(){
        StackPane root = new StackPane();
        scene = new Scene(root, 400, 600);
        scene.onKeyPressedProperty();
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }
    
}
