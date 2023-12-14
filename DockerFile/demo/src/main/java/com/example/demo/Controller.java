package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import static java.lang.System.*;

@RestController
public class Controller {

    @GetMapping("/")
    public String saludo() {
        return "Hola Mundo";
    }
}
