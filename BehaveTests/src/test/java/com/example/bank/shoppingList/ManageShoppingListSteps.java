package com.example.bank.shoppingList;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.shoppingList.ShoppingItem;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.restassured.RestAssured;
import io.restassured.http.ContentType;

import java.util.Arrays;
import java.util.List;

import static com.shoppingList.Config.API;
import static net.serenitybdd.rest.SerenityRest.*;
import static org.junit.Assert.*;

public class ManageShoppingListSteps {

    private final ObjectMapper mapper = new ObjectMapper();

    private String userIdn;
    private ShoppingItem shoppingItem;

    public void deleteCurrentShoppingItem() {
        RestAssured.given()
            .contentType(ContentType.JSON)
            .pathParam("itemId", this.shoppingItem.getId())
            .delete(API + "/item/{itemId}")
            .then()
            .statusCode(204);
    }

    @Given(" user identifier: {0}")
    public void givenUserIdentifier(String userIdn) {
        this.userIdn = userIdn;
    }

    @When(" get current shopping list")
    public void whenGetCurrentShoppingList() {
        given()
            .contentType(ContentType.JSON)
            .get(API + "/items");
    }

    @When(" create shopping element list with name: {0}")
    public void whenCreateShoppingListElementWithName(String name) {
        String jsonRequest = "";
        try {
            jsonRequest = mapper.writeValueAsString(ShoppingItem.builder().name(name).build());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
        String jsonResponse = given()
            .contentType(ContentType.JSON)
            .body(jsonRequest)
            .post(API + "/item")
        .then()
            .statusCode(201)
        .extract().response().asString();

        try {
            this.shoppingItem = mapper.readValue(jsonResponse, ShoppingItem.class);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @When(" remove shopping element list")
    public void whenRemoveShoppingListElement() {
        given()
            .contentType(ContentType.JSON)
            .pathParam("itemId", this.shoppingItem.getId())
            .delete(API + "/item/{itemId}")
            .then()
            .statusCode(204);
    }

    @When(" change product buy status in the shopping list element from: {0}")
    public void whenChangeProductBuyStatusInTheShoppingListElement(boolean buyStatus) {
        given()
            .contentType(ContentType.JSON)
            .pathParam("itemId", this.shoppingItem.getId())
            .put(API + "/item/{itemId}/changeBuyStatus")
            .then()
            .statusCode(201);
    }

    @When(" change product amount in the shopping list element to: {0}")
    public void whenChangeProductAmountInTheShoppingListElement(int amount) {
        String jsonRequest = "";
        try {
            jsonRequest = mapper.writeValueAsString(ShoppingItem.builder().amount(amount).build());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }

        given()
            .contentType(ContentType.JSON)
            .body(jsonRequest)
            .pathParam("itemId", this.shoppingItem.getId())
            .put(API + "/item/{itemId}/changeAmount")
            .then()
            .statusCode(201);
    }

    @Then(" result should contains shopping list elements")
    public void thenResultShouldContainsShoppingListElements() {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<ShoppingItem> shoppingList = Arrays.asList(mapper.readValue(json, ShoppingItem[].class));
            assertFalse(shoppingList.isEmpty());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @Then(" result should contains appropriate shopping list element with name: {0}")
    public void thenResultShouldContainsShoppingListElementWithName(String name) {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<ShoppingItem> shoppingList = Arrays.asList(mapper.readValue(json, ShoppingItem[].class));
            assertTrue(shoppingList.stream().anyMatch(item -> item.getName().equals(name)));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @Then(" result should not contains appropriate shopping list element with name: {0}")
    public void thenResultShouldNotContainsShoppingListElementWithName(String name) {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<ShoppingItem> shoppingList = Arrays.asList(mapper.readValue(json, ShoppingItem[].class));
            assertFalse(shoppingList.stream().anyMatch(item -> item.getName().equals(name)));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @Then(" result should contains appropriate shopping list element with buy status: {0}")
    public void thenResultShouldContainsShoppingListElementWithBuyStatus(boolean buyStatus) {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<ShoppingItem> shoppingList = Arrays.asList(mapper.readValue(json, ShoppingItem[].class));
            assertEquals(shoppingList.stream()
                .filter(item -> item.getId().equals(this.shoppingItem.getId()))
                .findAny().map(ShoppingItem::getBought).orElse(false), buyStatus);
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @Then(" result should contains appropriate shopping list element with amount: {0}")
    public void thenResultShouldContainsShoppingListElementWithAmount(int amount) {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<ShoppingItem> shoppingList = Arrays.asList(mapper.readValue(json, ShoppingItem[].class));
            assertEquals(shoppingList.stream()
                .filter(item -> item.getId().equals(this.shoppingItem.getId()))
                .findAny().map(ShoppingItem::getAmount).orElse(0), Integer.valueOf(amount));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

}
