package com.huaweicloud.aom;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    

    @RequestMapping("/")
    String hello() {
        return "Hello World!";
    }
}
