package org.goomez;

import javax.swing.*;
import java.awt.*;

public class jFrame01 {
    static void main() {
        JFrame frame = new JFrame(); // create frame
        frame.setTitle("Primary frame"); // set title of frame
        frame.setSize(400, 400); // set the x and y dimension
        frame.setResizable(false); // prevent frame from being resized
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE); // exit out of application
        frame.setVisible(true); // make frame visible

        ImageIcon image = new ImageIcon("Local da imagem"); // create an ImageIcon
        frame.setIconImage(image.getImage()); // change icon of frame
        frame.getContentPane().setBackground(new Color(255, 255, 255)); // change color of background
    }
}
