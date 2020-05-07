package com.example.fn;
import com.fnproject.fn.api.FnConfiguration;
import com.fnproject.fn.api.RuntimeContext;

public class HelloFunction {
    private String user,driver,url, password;
    @FnConfiguration
    public void config(RuntimeContext ctx) {
     url=ctx.getConfigurationByKey("DB_URL").orElse("jdbc:oracle");
     driver=ctx.getConfigurationByKey("DB_DRIVER").orElse("OracleDriver");
     user=ctx.getConfigurationByKey("DB_USER").orElse("admin");
    }
    public String handleRequest(String input) {
        String name = (input == null || input.isEmpty()) ? "world"  : input;
        return "Hello, " + name + "!";
    }
    public String getConnection() {
    return "  driver.... "+driver +" user..  "+user +" URL ..." +url;
}
}
