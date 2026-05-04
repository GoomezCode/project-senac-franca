package org.goomez.initspring.exception;

public class firstException extends Exception {
    public firstException(String msg){
        msg = (!msg.equals("")?msg :" Alguem erro ai!!");
        super(msg);
    }

}
