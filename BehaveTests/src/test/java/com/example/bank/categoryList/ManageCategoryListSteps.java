package com.example.bank.categoryList;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.shoppingList.Category;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.restassured.http.ContentType;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;

import static com.shoppingList.Config.API;
import static net.serenitybdd.rest.SerenityRest.given;
import static net.serenitybdd.rest.SerenityRest.then;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class ManageCategoryListSteps {

    private final ObjectMapper mapper = new ObjectMapper();

    @When(" get current category list")
    public void whenGetCurrentCategoryList() {
        given()
            .contentType(ContentType.JSON)
            .get(API + "/category/all");
    }

    @Then(" result should contains category list")
    public void thenResultShouldContainsCategoryList() {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<Category> categories = Arrays.asList(mapper.readValue(json, Category[].class));
            assertFalse(categories.isEmpty());
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

    @Then(" result should contains products for category id: {0}")
    public void thenResultShouldContainsProductsForCategoryId(Long categoryId) {
        String json = then().statusCode(200).extract().response().asString();
        try {
            List<Category> categories = Arrays.asList(mapper.readValue(json, Category[].class));
            assertTrue(categories.stream()
                .filter(category -> category.getId().equals(categoryId))
                .map(Category::getProducts)
                .flatMap(Collection::stream)
                .allMatch(product -> product.getCategoryId().equals(categoryId)));
        } catch (JsonProcessingException e) {
            e.printStackTrace();
        }
    }

}
