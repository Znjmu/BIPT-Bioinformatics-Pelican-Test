# Publishing this release on GitHub

> [!IMPORTANT]
> Publish **the public-release folder**, not any separate active benchmark
> organizer/private ZIP. **Do not include active hidden seeds or answer keys**
> if you intend to continue testing on the same benchmark.

## Option A — GitHub website

1. Create a new repository (for example, `BIPT-Bioinformatics-Pelican-Test`).
2. Choose public visibility if you want the material accessible to everyone.
3. Upload **the contents of the `BIPT_v1_GitHub_Release` folder**, preserving
   `README.md` at the repository root, not the folder as an extra nested level.
4. Verify that the two images render, the links in the README work, and the
   leaderboard CSV and JSON open.
5. Add a repository description, topics such as `bioinformatics`,
   `ai-evaluation`, `genomics`, `benchmark`, `vcf`, and `reproducibility`.
6. Before claiming a formal release, choose a license. No license is presumed
   by this package. GitHub public visibility **does not automatically grant a
   software redistribution license**. The benchmark author may select a
   suitable license (e.g. MIT for original code, CC BY 4.0 for documentation).
7. Create a versioned GitHub Release for `v1.0` and archive a checksum list.

## Option B — Command line

```bash
cd /path/to/BIPT_v1_GitHub_Release
git init
git add .
git commit -m "Publish BIPT v1.0 methodology and results"
git branch -M main
# Create an EMPTY GitHub repository first.
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

**Do not paste private tokens** into markdown files or commit history.

## Optional: full scoring-source publication

The companion `BIPT_v1_Full_Reproducibility_ARCHIVE.zip` contains the
retrospective grading source and original v1.0 synthetic-data generator.
Publishing that package exposes the historic hidden cases and invalidates
**any future blinded reuse of the same v1.0 benchmark**. It is appropriate
only as an archive of a **retired** benchmark version. Develop a new secret
held-out generation scheme before any future competitive evaluations.

> [!CAUTION]
> The original 11 complete candidate source archives are not included in the
> GitHub release. Full replay of historical model-specific scores requires
> those original submissions and the disclosed scoring environment.
