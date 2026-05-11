package org.goomez;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class jLabel01 {
    static void main() {
        Border border = BorderFactory.createLineBorder(Color.black);
        JLabel txt01 =  new JLabel(); // create a label
        txt01.setText("Hello World"); // set text of label
        txt01.setHorizontalAlignment(JLabel.CENTER);
        txt01.setForeground(Color.black); // set color text
        txt01.setFont(new Font("Times New Roman", Font.BOLD, 20));
        txt01.setBorder(border);


        jFrame01 frame = new jFrame01();
        frame.getContentPane().setBackground(Color.white);
        frame.add(txt01);
        frame.setVisible(true);
    }
}
