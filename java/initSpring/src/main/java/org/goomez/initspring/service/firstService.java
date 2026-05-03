package org.goomez.initspring.service;

import org.springframework.stereotype.Service;

@Service
public class firstService {
    public static String first(String name){
        return "first Hello World! "+ name;
    }
}
