package org.goomez.initspring.controller.pages;

import org.goomez.initspring.controller.firstController;
import org.goomez.initspring.exception.firstException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@Controller
@RequestMapping("/page")
public class pageIndex {
    @Autowired
    firstController tst;

    @GetMapping
    public String teste(Model model, @RequestParam(value="nome", defaultValue ="Errado") String nome) throws firstException {
        try {
            String name = nome;
            if (!name.equalsIgnoreCase("daniel")) {
                throw new firstException("Erooo");
            }
            model.addAttribute("name", name);
            return "page";
        }catch (firstException e){
            System.err.println("Erro geral ao efetuar o login: "+ e.getMessage());
            return "error";
        }
    }
}
