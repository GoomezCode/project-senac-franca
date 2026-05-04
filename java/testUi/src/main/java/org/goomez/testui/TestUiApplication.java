package org.goomez.testui;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;

@SpringBootApplication
public class TestUiApplication {
    public static void main(String[] args) {
        new SpringApplicationBuilder(TestUiApplication.class)
                .headless(false)
                .run(args);
    }

}
