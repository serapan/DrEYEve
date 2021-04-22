describe('Navigation Drawer', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    describe('should have valid structure', () => {
        it('should contain main nav icon', () => {
            cy.get('#main-nav-icon').should('exist');
            cy.get('#main-nav-icon').should('be.visible');
        });

        it('should contain main nav drawer', () => {
            cy.get('#main-nav-drawer').should('exist');
            cy.get('#main-nav-drawer').should('not.be.visible');
        });

        it('should contain main nav user', () => {
            cy.get('#main-nav-drawer #main-nav-user').should('exist');
            cy.get('#main-nav-drawer #main-nav-user').should('not.be.visible');
        });

        it('should contain main nav items', () => {
            cy.get('#main-nav-drawer #main-nav-items').should('exist');
            cy.get('#main-nav-drawer #main-nav-items').should('not.be.visible');
        });

        it('should contain 2 nav items', () => {
            cy.get('#main-nav-items .main-nav-item').should('exist');
            cy.get('#main-nav-items .main-nav-item').should($el => {
                expect($el).to.have.length(2);
            });
        });

        describe('when closed', () => {
            it('close nav drawer should be hidden', () => {
                cy.get('#button-nav-drawer-close').should('be.hidden');
            });

            it('nav user should be hidden', () => {
                cy.get('#main-nav-user').should('be.hidden');
            });

            it('nav items should be hidden', () => {
                cy.get('#main-nav-items').should('be.hidden');
                cy.get('#main-nav-items .main-nav-item').should('be.hidden');
            });
        });

        describe('when open', () => {
            beforeEach(() => {
                cy.get('#main-nav-icon').trigger('click');
            });

            afterEach(() => {
                cy.get('#button-nav-drawer-close').trigger('click');
            });

            it('close nav drawer should be visible', () => {
                cy.get('#button-nav-drawer-close').should('be.visible');
            });

            it('nav user should be visible', () => {
                cy.get('#main-nav-user').should('be.visible');
            });

            it('nav items should be visible', () => {
                cy.get('#main-nav-items').should('be.visible');
                cy.get('#main-nav-items .main-nav-item').should('be.visible');
            });
        });
    });

    describe('should have valid functionality', () => {
        beforeEach(() => {
            cy.get('#main-nav-icon').trigger('click');
        });

        it('should display about view', () => {
            cy.get('#main-nav-item-about').trigger('click');
            cy.contains('This is an about page');
        });
        
        it('should display home view', () => {
            cy.get('#main-nav-item-home').trigger('click');
            cy.contains('Welcome from Vue TypeScript App!');
        });
    });
});