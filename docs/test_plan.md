# Test Plan

**Project:** Tagsbase - Fashion Brand Directory  
**Test Plan Identifier:** TAGSBASE-TP-001
**Version:** 1.0  
**Date:** January 22, 2026  
**Author:** Denis Ivliushkin

## 1. References

- GitHub Repository: [tagsbase-tests](https://www.github.com/ivliushkin/tagsbase-tests)
- Application: [TagsBase.com](https://www.tagsbase.com)
- Tools & Frameworks: Python, Flask, pytest, GitHub Actions
- IEEE Std 829 (for structure reference)

## 2. Introduction

**TagsBase** is a small learning project and brand directory. I use this website to practice software testing, QA, and CI/CD on a real project. It is a sandbox where I test ideas, try new tools, and learn how software is built and deployed step by step.

Purpose of testing is to ensure the Tagsbase MVP:

- correctly displays fashion brand information
- supports basic navigation and discovery flows
- contains no critical functional defects or obvious regressions
- remains stable after each deployment (GitHub Actions + Hosting)

## 3. Test Items

- Flask API endpoints and page logic (backend controllers)
- Web UI layouts and dynamic data rendering (Jinja2 templates)
- Data integrity for "Brands" and "Categories" tables (SQlite)
- Frontend static files (CSS styles, icons, and images)
- Automated build and deployment workflows (GitHub Actions YAML)

## 4. Features to be Tested

- Core user ways (home page → brand discovery → brand detail page)
- All implemented Flask routes and templates
- Responsive layout on desktop and mobile (basic check)
- Data correctness of brands that are already added
- CI/CD pipeline stability (tests pass → auto-deploy)

## 5. Features Not to Be Tested

- Advanced search / full-text search
- Admin panel / content management
- Performance & load testing (> 100 concurrent users)
- Accessibility (WCAG)
- Internationalization / multi-language
- Security audit (OWASP Top 10 deep check)
- SEO deep analysis

## 6. Approach

### Testing Types

**Functional Testing:** Positive (happy paths, e.g., search and navigation work correctly) and Negative (errors, e.g., invalid search or broken links).

**UI Validation:** Checking Jinja2 template rendering, CSS styles, and dynamic data.

**Smoke and Functional Tests:** Mixed approach — automation for basic scenarios + manual checks for UI and user flows.

**Compatibility Tests:** Basic checks for compatibility (desktop and mobile browsers/devices).

**Data Correctness:** Verifying data integrity in SQLite (brands, categories) through queries and assertions.

**Regression Testing:** Automated tests in CI to prevent regressions after changes.

**Non-Functional Testing (Basic):** Light checks for performance (load time < 3s) and SEO (meta tags, sitemap). Deep audits are deferred (see Section 5).

### Automation

Pytest suite runs on every push/PR in GitHub Actions.
If tests fail, deployment is blocked.

### Manual Testing

_After each deploy:_ Smoke checklist for key flows (home → search → brand page) + main negative cases.
_Dev tools_ for inspection (console errors, network requests).
**Frequency:** Weekly or after significant changes for manual checks.

### Tools

**Automation:** pytest (for unit/integration), requests (for API-like checks).
**Manual/Debug:** Browser dev tools (Chrome/Firefox), mobile emulators.
**CI/CD:** GitHub Actions for running tests and deployment.

## 7. Item Pass/Fail Criteria

- Pass: All automated tests green, no P0/P1 defects found in smoke, page load < 3s (subjective), no console errors.
- Fail: Any critical bug (500 error, wrong data display, broken navigation) → rollback / fix required before considering "ready".

## 8. Suspension Criteria and Resumption Requirements

Suspension: critical bug blocks core flow → fix + re-run CI
Resumption: new commit with fix → CI green + quick manual smoke

## 9. Test Deliverables

**Automated:**
pytest suite (unit + simple functional / integration tests)

**Manual (checklist):**
Smoke / happy-path checklist

**Bug report template** (if critical bug found - title, steps, actual/expected, screenshots)

**Test report**

## 10. Environmental Needs

- **Production** —[TagsBase.com](https://tagsbase.com)
- **Local** — Flask development server
- **Browsers:** Chrome (latest), Firefox (latest), Safari (latest), mobile Chrome/Safari
- **OS:** macOS, iOS

## 11. Risks and Contingencies

| Risk                                   | Probability | Impact | Mitigation                             |
| -------------------------------------- | ----------- | ------ | -------------------------------------- |
| Database data becomes outdated         | Medium      | High   | Manual check                           |
| Hosting limits / downtime              | Low         | Medium | Set up and receive notifications       |
| Very slow page load due to many images | Medium      | Medium | Lazy loading (future), compress images |
| Broken tests block deployment          | Medium      | High   | Keep tests simple & stable             |

## 12. Approvals

`Prepared by:` Denis Ivliushkin (_personal project_)  
`Date:` January 22, 2026
