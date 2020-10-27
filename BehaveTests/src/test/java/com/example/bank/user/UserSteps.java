package com.example.bank.user;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.shoppingList.User;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.restassured.http.ContentType;

import static com.shoppingList.Config.API;
import static net.serenitybdd.rest.SerenityRest.given;
import static net.serenitybdd.rest.SerenityRest.then;
import static org.junit.Assert.assertEquals;

public class UserSteps {

    private final ObjectMapper mapper = new ObjectMapper();

    private String login;

    @Given(" user login: {0}")
    public void givenUserLogin(String login) {
        this.login = login;
    }

    @When(" get user data for chosen login")
    public void whenGetUserDataForChosenLogin() {
        given()
            .contentType(ContentType.JSON)
            .get(API + "/user/" + login);
    }

    @Then(" result should contains data for current user")
    public void thenResultShouldContainsDataForCurrentUser() {
        String json = then().statusCode(200).extract().response().asString();
        try {
            User user = mapper.readValue(json, User.class);
            assertEquals(login, user.getLogin());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

}
