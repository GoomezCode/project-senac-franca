package org.goomez.initspring.controller;

import org.goomez.initspring.model.user;
import org.goomez.initspring.service.firstService;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/first")
public class firstController {
    @GetMapping
    public String Helloworld() {
        return firstService.first("Daniel");
    }

    @PostMapping("/{id}")
    public String HelloWorldPost(@PathVariable("id") String id,@RequestParam(value="nome", defaultValue = "errado")String nome, @RequestBody user body){
        return "Hello World! "+ body.getNome() + id + nome ;
    }

}
