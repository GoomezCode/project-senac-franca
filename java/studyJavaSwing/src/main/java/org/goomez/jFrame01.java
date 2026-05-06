package org.goomez;

import javax.swing.*;
import java.awt.*;

public class jFrame01 extends JFrame {
    jFrame01() {
        this.setTitle("Primary frame"); // set title of frame
        this.setSize(400, 400); // set the x and y dimension
        //this.setResizable(false); // prevent frame from being resized
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE); // exit out of application
        // this.setVisible(true); // make frame visible

        ImageIcon image = new ImageIcon("Local da imagem"); // create an ImageIcon
        this.setIconImage(image.getImage()); // change icon of frame
        this.getContentPane().setBackground(new Color(255, 255, 255)); // change color of background
    }
}
