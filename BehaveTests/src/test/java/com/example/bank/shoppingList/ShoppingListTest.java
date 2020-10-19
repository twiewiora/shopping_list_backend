package com.example.bank.shoppingList;

import net.serenitybdd.junit.runners.SerenityRunner;
import net.thucydides.core.annotations.Steps;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(SerenityRunner.class)
public class ShoppingListTest {

    @Steps
    private ManageShoppingListSteps manageShoppingListSteps;

    @Test
    public void shouldReturnShoppingListProducts() {
        manageShoppingListSteps.givenUserIdentifier("test");

        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElements();
    }

    @Test
    public void shouldAddProductToShoppingList() {
        manageShoppingListSteps.givenUserIdentifier("test");

        manageShoppingListSteps.whenCreateShoppingListElementWithName("test");
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElementWithName("test");

        manageShoppingListSteps.deleteCurrentShoppingItem();
    }

    @Test
    public void shouldAddAndRemoveProductFromShoppingList() {
        manageShoppingListSteps.givenUserIdentifier("test");

        manageShoppingListSteps.whenCreateShoppingListElementWithName("test");
        manageShoppingListSteps.whenRemoveShoppingListElement();
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldNotContainsShoppingListElementWithName("test");
    }

    @Test
    public void shouldChangeProductBuyStatusInTheShoppingList() {
        manageShoppingListSteps.givenUserIdentifier("test");

        manageShoppingListSteps.whenCreateShoppingListElementWithName("test");
        manageShoppingListSteps.whenChangeProductBuyStatusInTheShoppingListElement(false);
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElementWithBuyStatus(true);

        manageShoppingListSteps.deleteCurrentShoppingItem();
    }

    @Test
    public void shouldChangeProductAmountInTheShoppingList() {
        manageShoppingListSteps.givenUserIdentifier("test");

        manageShoppingListSteps.whenCreateShoppingListElementWithName("test");
        manageShoppingListSteps.whenChangeProductAmountInTheShoppingListElement(5);
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElementWithAmount(5);

        manageShoppingListSteps.deleteCurrentShoppingItem();
    }

}