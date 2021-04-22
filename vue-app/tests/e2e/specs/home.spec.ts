describe('Home Page', () => {
    beforeEach(() => {
        cy.visit('/');
    });

    describe('should have valid structure', () => {
        it('title should be valid', () => {
            cy.title().should('contain', 'vue-app');
        });

        it('should have header', () => {
            cy.get('#main-app-header').should('exist');
        });

        it('should have footer', () => {
            cy.get('#main-app-footer').should('exist');
        });

        it('should contain main nav icon', () => {
            cy.get('#main-nav-icon').should('exist');
            cy.get('#main-nav-icon').should('be.visible');
        });

        it('should contain main logo', () => {
            cy.get('#main-logo').should('exist');
            cy.get('#main-logo').should('be.visible');
        });

        it('should contain main title', () => {
            cy.get('#main-title').should('exist');
            cy.get('#main-title').should('be.visible');
            cy.get('#main-title').contains('Vue App');
        });

        it('should contain about button', () => {
            cy.get('#button-about').should('exist');
            cy.get('#button-about').should('be.visible');
        });

        it('should contain main nav drawer', () => {
            cy.get('#main-nav-drawer').should('exist');
            cy.get('#main-nav-drawer').should('not.be.visible');
        });

        it('footer should contain copyright', () => {
            cy.get('#main-app-footer').contains('©');
        });

        it('footer should contain current year', () => {
            const curDate: Date = new Date();
            cy.get('#main-app-footer').contains(curDate.getFullYear());
        });

        it('should display welcome message', () => {
            cy.contains('Welcome from Vue TypeScript App!');
        });
    });

    describe('should have valid functionality', () => {
        it('should open nav drawer', () => {
            cy.get('#main-nav-icon').trigger('click');
            cy.get('#main-nav-drawer').should('be.visible');
        });

        it('should close nav drawer', () => {
            cy.get('#main-nav-icon').trigger('click');
            cy.get('#main-nav-drawer').should('be.visible');
            cy.get('#button-nav-drawer-close').trigger('click');
            cy.get('#main-nav-drawer').should('not.be.visible');
        });

        it('should display about view', () => {
            cy.get('#button-about').trigger('click');
            cy.contains('This is an about page');
        });
        
        it('should display home view', () => {
            cy.get('#main-logo').trigger('click');
            cy.contains('Welcome from Vue TypeScript App!');
        });
    });
});
