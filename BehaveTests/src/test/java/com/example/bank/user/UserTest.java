package com.example.bank.user;

import net.serenitybdd.junit.runners.SerenityRunner;
import net.thucydides.core.annotations.Steps;
import org.junit.Test;
import org.junit.runner.RunWith;

import static com.shoppingList.Config.TEST_USER_LOGIN;

@RunWith(SerenityRunner.class)
public class UserTest {

    @Steps
    private UserSteps userSteps;

    @Test
    public void shouldReturnUserDataForGivenLogin() {
        userSteps.givenUserLogin(TEST_USER_LOGIN);
        userSteps.whenGetUserDataForChosenLogin();
        userSteps.thenResultShouldContainsDataForCurrentUser();
    }

}
