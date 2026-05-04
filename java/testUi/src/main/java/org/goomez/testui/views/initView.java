package org.goomez.testui.views;

import org.goomez.testui.views.page.Main;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class initView implements CommandLineRunner {

    @Override
    public void run(String... args) throws Exception {
        Main.main(args);
    }


}
