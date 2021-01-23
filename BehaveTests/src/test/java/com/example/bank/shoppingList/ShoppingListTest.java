package com.example.bank.shoppingList;

import net.serenitybdd.junit.runners.SerenityRunner;
import net.thucydides.core.annotations.Narrative;
import net.thucydides.core.annotations.Steps;
import org.junit.Test;
import org.junit.runner.RunWith;

import static com.shoppingList.Config.TEST_USER_LOGIN;

@RunWith(SerenityRunner.class)
@Narrative(title = "Tytuł", text = "aslkdjalksmdlkas")
public class ShoppingListTest {

    @Steps
    private ManageShoppingListSteps manageShoppingListSteps;

    private final String productName = "testProduct";

    @Test
    public void shouldReturnShoppingListProductsForUser() {
        manageShoppingListSteps.givenUserIdentifier(TEST_USER_LOGIN);

        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElements();
    }

    @Test
    public void shouldAddProductToShoppingList() {
        manageShoppingListSteps.givenUserIdentifier(TEST_USER_LOGIN);

        manageShoppingListSteps.whenCreateShoppingListElementWithName(productName);
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElementWithName(productName);

        manageShoppingListSteps.deleteCurrentShoppingItem();
    }

    @Test
    public void shouldAddAndRemoveProductFromShoppingList() {
        manageShoppingListSteps.givenUserIdentifier(TEST_USER_LOGIN);

        manageShoppingListSteps.whenCreateShoppingListElementWithName(productName);
        manageShoppingListSteps.whenRemoveShoppingListElement();
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldNotContainsShoppingListElementWithName(productName);
    }

    @Test
    public void shouldChangeProductBuyStatusInTheShoppingList() {
        manageShoppingListSteps.givenUserIdentifier(TEST_USER_LOGIN);

        manageShoppingListSteps.whenCreateShoppingListElementWithName(productName);
        manageShoppingListSteps.whenChangeProductBuyStatusInTheShoppingListElement();
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElementWithBuyStatus(true);

        manageShoppingListSteps.deleteCurrentShoppingItem();
    }

    @Test
    public void shouldChangeProductAmountInTheShoppingList() {
        manageShoppingListSteps.givenUserIdentifier(TEST_USER_LOGIN);

        manageShoppingListSteps.whenCreateShoppingListElementWithName(productName);
        manageShoppingListSteps.whenChangeProductAmountInTheShoppingListElement(5);
        manageShoppingListSteps.whenGetCurrentShoppingList();

        manageShoppingListSteps.thenResultShouldContainsShoppingListElementWithAmount(5);

        manageShoppingListSteps.deleteCurrentShoppingItem();
    }

}