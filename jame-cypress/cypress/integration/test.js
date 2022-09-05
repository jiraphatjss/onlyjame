describe('open and check "Contain" on this website', () => {
  it('open thsi website', () => {
    cy.visit('https://leelaella.com/')
    cy.get('data-cy="nav-blog"').click()
  })
})

