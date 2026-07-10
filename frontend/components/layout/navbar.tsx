"use client"

import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
import { Button } from "@/components/ui/button"
import Link from "next/link"
import {Moon, Sun} from "lucide-react"
import { useTheme } from "next-themes"

export default function Navbar() {

  const { resolvedTheme, setTheme } = useTheme()

  return (
    <nav className="p-8">
      <NavigationMenu>
        <NavigationMenuList>
          <NavigationMenuLink 
          className="font-bold mr-6 text-xl"
          render={<Link href="/"/>}
          >
            APB Trainer v2
          </NavigationMenuLink>
          <NavigationMenuItem>
            <NavigationMenuTrigger>Learn</NavigationMenuTrigger>
            <NavigationMenuContent>
              <NavigationMenuLink
                render={<Link href="/learn/lxs-algorithms" />}
              >
                LXS Algorithms
              </NavigationMenuLink>
              <NavigationMenuLink
                render={<Link href="/learn/eo-pair-algorithms" />}
              >
                EO Pair Algorithms
              </NavigationMenuLink>
            </NavigationMenuContent>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <NavigationMenuTrigger>Practice</NavigationMenuTrigger>
            <NavigationMenuContent>
              <NavigationMenuLink
                render={<Link href="/practice/lxs-trainer" />}
              >
                LXS Trainer
              </NavigationMenuLink>
              <NavigationMenuLink
                render={<Link href="/practice/eo-pair-trainer" />}
              >
                EO Pair Trainer
              </NavigationMenuLink>
            </NavigationMenuContent>
          </NavigationMenuItem>
          <Button variant="outline" className="ml-6" onClick={() => setTheme(resolvedTheme === "dark" ? "light" : "dark")}>
            <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
            <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
          </Button>
        </NavigationMenuList>
      </NavigationMenu>
    </nav>
  )
}