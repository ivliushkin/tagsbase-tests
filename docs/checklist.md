# Checklist: Tagsbase

This document contains checklists for manual and automated verification.

**Legend:** [P0] critical, [P1] high, [P2] medium

## 1. Homepage & Navigation

- [ ] Verify that the "Hero" section displays (title, subtitle, buttons, links)
- [ ] Verify that "Latest Added" section shows 5 most recent brands
- [ ] Verify that "Explore by category" tiles lead to the correct filtered pages
- [ ] Check if the Navbar links (Home, All Brands) are working
- [ ] Verify the Footer contains legal link and the correct current year
- [ ] Verify that the home page addapts on mobile

## 2. Brand Catalog & Search

- [ ] Verify A-Z filter: clicking a letter shows only brands starting with that letter.
- [ ] Verify "View All" button resets all filters.
- [ ] **Search:**
  - [ ] Search by full name (e.g., "ASICS") returns the correct brand.
  - [ ] Search by partial name (e.g., "AS") returns matching results.
  - [ ] Search for a non-existent brand shows the "No brands found" message.
- [ ] Verify category filtering (Shoes, Clothing, Accessories).

## 3. Brand Details (The "Product" Page) & SEO

- [ ] Verify all fields are present: Name, Description, Country, Year, Type.
- [ ] Verify the "Return to catalog" link works and remembers the previous filter (via `next` param).
- [ ] **SEO Check:**
  - Verify that `<title>` and `<meta description>` change according to the brand.
  - [ ] Verify JSON-LD Schema.org script is present in the source code.

## 4. Contact Form (Data Validation)

- [ ] Submit empty form: error messages should appear for required fields.
- [ ] Submit message < 10 characters: validation error should trigger.
- [ ] Submit valid data: verify success message and (simulated) email delivery.

## 5. Admin Analytics & Security

- [ ] Access to admin panels should be visible with proper credentials(optional)
- [ ] Verify 404 page triggers for any invalid URL.
