package com.example.bank.categoryList;

import net.serenitybdd.junit.runners.SerenityRunner;
import net.thucydides.core.annotations.Steps;
import org.junit.Test;
import org.junit.runner.RunWith;

@RunWith(SerenityRunner.class)
public class CategoryListTest {

    @Steps
    private ManageCategoryListSteps manageCategoryListSteps;

    @Test
    public void shouldReturnCategoryList() {
        manageCategoryListSteps.whenGetCurrentCategoryList();

        manageCategoryListSteps.thenResultShouldContainsCategoryList();
    }

    @Test
    public void shouldReturnProductListByForGivenCategory() {
        manageCategoryListSteps.whenGetCurrentCategoryList();

        manageCategoryListSteps.thenResultShouldContainsProductsForCategoryId(1L);
    }

}
